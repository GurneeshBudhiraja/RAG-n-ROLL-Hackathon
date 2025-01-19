import streamlit as st
import os
from dotenv import load_dotenv
import snowflake.connector
import string, random
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

connection_object = snowflake.connector.connect(
    user=os.environ.get("SNOWFLAKE_USER"),
    password=os.environ.get("SNOWFLAKE_PASSWORD"),
    account=os.environ.get("SNOWFLAKE_USER_ACCOUNT"),
    warehouse=os.environ.get("WAREHOUSE"),
    database="DOCUMENT_DECODER",
    schema="DATA",
)

cursor = connection_object.cursor()


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
    try:
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
                upload_document(table_name=table_name)

            st.session_state.state["processing"] = False
            st.session_state.state["chat_ready"] = True
            st.session_state.state["first_part_visible"] = False
            st.rerun()
    except Exception as e:
        print(f"Error in first_part: {str(e)}")
        st.error("An error occurred. Please try again.")


# This is the starter function
def upload_document(table_name):
    """
    Saves the uploaded file to a temporary directory
    and uploads it to Snowflake transient table.
    """
    try:
        print("TABLE_NAME", table_name)

        # Gets and save the file on the machine
        streamlit_file = st.session_state.state["file_uploaded"]
        local_file_path = os.path.join("temp_dir", streamlit_file.name)
        os.makedirs("temp_dir", exist_ok=True)

        with open(local_file_path, "wb") as f:
            f.write(streamlit_file.read())

        print("================ Uploading file ===========================")
        upload_pdf_with_metadata(table_name=table_name, pdf_path=local_file_path)

        # Creates the cortex search service
        print(
            "================ creating cortex search service ==========================="
        )
        cortex_search_response = create_cortex_service(table_name=table_name)
        print("Cortex search response:", cortex_search_response)
        print(
            "================ END :: creating cortex search service :: END ==========================="
        )

        # remove the file from the system
        os.remove(local_file_path)
    except Exception as e:
        print(f"Error uploading document: {str(e)}")
        return False


def upload_pdf_with_metadata(table_name: str, pdf_path: str):
    try:
        # Create a more detailed table
        create_table_query = f"""
            create or replace TRANSIENT TABLE {table_name} ( 
            FILE_NAME VARCHAR,
            CHUNK_ID NUMBER,
            CHUNK_TEXT VARCHAR(16777216),
            PAGE_NUMBER NUMBER,
            CHUNK_SIZE NUMBER
        );
        """

        cursor.execute(create_table_query)

        # Load and split PDF
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        chunks = text_splitter.split_documents(pages)

        # Insert chunks with metadata
        file_name = os.path.basename(pdf_path)
        for chunk_id, chunk in enumerate(chunks):
            insert_query = f"""
            INSERT INTO {table_name} 
            (FILE_NAME, CHUNK_ID, CHUNK_TEXT, PAGE_NUMBER, CHUNK_SIZE)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(
                insert_query,
                (
                    file_name,
                    chunk_id,
                    chunk.page_content,
                    chunk.metadata.get("page", 0),
                    len(chunk.page_content),
                ),
            )

        return True

    except Exception as e:
        print(f"Error uploading chunks: {str(e)}")
        return False


def create_cortex_service(table_name):
    query = f"""
    create or replace CORTEX SEARCH SERVICE {table_name}_CS
    ON chunk_text
    warehouse = COMPUTE_WH
    TARGET_LAG = '1 minute'
    as (
        select chunk_text, file_name
        from {table_name}
        );
    """
    print("Creating cortex service")
    cortex_search_response = cursor.execute(query)
    return cortex_search_response


# Generate random table names
def generate_random_string(length=18):
    characters = string.ascii_letters
    random_string = "".join(random.choices(characters, k=length))
    return random_string


if __name__ == "__main__":
    table_name = generate_random_string()
    upload_document(table_name=table_name)
