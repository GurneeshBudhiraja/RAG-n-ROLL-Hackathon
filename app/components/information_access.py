import streamlit as st
from app.cortex_search.information_access_search import information_access_search
from app.constants.information_access_constants import information_access_content


def information_access(selected_language):
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "static/farmer-standing.jpg",
            use_container_width=True,
        )
    with col2:
        st.header(information_access_content[selected_language]["header"])

    st.write(information_access_content[selected_language]["description"])

    # Selectbox
    categories = [
        "Government Schemes",
        "NGOs and Organizations",
        "Helplines and Contacts",
    ]
    selected_category = st.selectbox(
        information_access_content[selected_language]["category_prompt"],
        categories,
        index=None,
        placeholder=information_access_content[selected_language][
            "category_placeholder"
        ],
    )

    user_question = st.text_input(
        information_access_content[selected_language]["input_prompt"],
        placeholder=information_access_content[selected_language]["input_placeholder"],
        key="enabled_input",
    )
    if user_question:

        if user_question:
            if not selected_category:
                st.error(information_access_content[selected_language]["error_message"])
            else:
                model_response = information_access_search(
                    user_question=user_question,
                    question_category=selected_category,
                    selected_langauge=selected_language,
                )
                if not model_response:
                    st.error("No results found.")
                else:
                    st.markdown(
                        information_access_content[selected_language]["question_header"]
                    )
                    st.markdown(f"###### {user_question}")
                    st.markdown(
                        information_access_content[selected_language]["answer_header"]
                    )
                    st.markdown(f"###### {model_response.strip()}")

        st.write("")
