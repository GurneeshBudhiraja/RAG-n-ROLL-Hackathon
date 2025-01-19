import streamlit as st
import os
from dotenv import load_dotenv
import snowflake.connector
import string, random

load_dotenv()

connection_object = snowflake.connector.connect(
    user=os.environ.get("SNOWFLAKE_USER"),
    password=os.environ.get("SNOWFLAKE_PASSWORD"),
    account="QPB44910",
    warehouse=os.environ.get("WAREHOUSE"),
    database="DOCUMENT_DECODER",
    schema="DATA",
)


def FileUploader():
    uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")
    return uploaded_file


def LanguageSelector():
    language_options = ["English", "Hindi", "Bengali"]
    selected_language = st.selectbox(
        "Choose a language for document processing:", language_options, index=None
    )
    return selected_language


def first_part():
    print("Session state\n", st.session_state.state)
    table_name = st.session_state.state["table_name"]
    (col1, _) = st.columns([1, 1])
    (col2, _) = st.columns([1, 1])

    with col1:
        uploaded_file = FileUploader()
        if uploaded_file:
            st.session_state.state["file_uploaded"] = uploaded_file

    with col2:
        if (
            st.session_state.state["file_uploaded"]
            and not st.session_state.state["language_selected"]
        ):
            selected_language = LanguageSelector()
            if st.button("Submit"):
                st.session_state.state["language_selected"] = selected_language
                st.session_state.state["processing"] = True

    if st.session_state.state["processing"]:
        with st.spinner("Processing your document..."):
            response = save_document()
            print("Temp db response:", response)

        st.session_state.state["processing"] = False
        st.session_state.state["chat_ready"] = True
        st.session_state.state["first_part_visible"] = False
        st.rerun()


def save_document():
    # Saves the doc to the local machine for snowflake stage
    table_name = st.session_state.state["table_name"]
    queries = [
        f"""
        CREATE OR REPLACE STAGE {table_name}_docs
        ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
        DIRECTORY = (ENABLE = TRUE);
        """
    ]
    streamlit_file = st.session_state.state["file_uploaded"]
    local_file_path = os.path.join("temp_dir", streamlit_file.name)
    os.makedirs("temp_dir", exist_ok=True)

    with open(local_file_path, "wb") as f:
        f.write(streamlit_file.read())

    absolute_path = os.path.abspath(local_file_path)
    formatted_path = absolute_path.replace("\\", "/")

    execute_query_response = execute_query(
        table_name=table_name, queries=queries, local_file_path=formatted_path
    )

    os.remove(local_file_path)

    return execute_query_response


def execute_query(table_name="", queries=[], local_file_path=None):
    try:
        if not queries:
            return False
        cursor = connection_object.cursor()
        stage_query = queries[0]
        print(f"Creating stage: {stage_query}")
        cursor.execute(stage_query)

        if local_file_path:
            print(f"Uploading file from: {local_file_path}")
            # Use the put_file method instead of execute for file uploads
            put_statement = (
                f"PUT file://{local_file_path} @{table_name}_docs AUTO_COMPRESS = FALSE"
            )
            cursor.execute(put_statement)
            result = cursor.fetchall()
            print("Upload result:", result)

        return True
    except Exception as e:
        print("Error in execute_query:", e)
        return False


# Generate random table name
def generate_random_string(length=18):
    characters = string.ascii_letters
    random_string = "".join(random.choices(characters, k=length))
    return random_string


if __name__ == "__main__":
    # table_name = generate_random_string()
    table_name = input("table name:").strip()
    print(
        execute_query(
            f"""
            CREATE TRANSIENT TABLE {table_name} (id NUMBER, creation_date DATE);
            """
        )
    )
