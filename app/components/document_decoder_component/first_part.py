import streamlit as st
import time


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
            time.sleep(5)
        st.session_state.state["processing"] = False
        st.session_state.state["chat_ready"] = True
        st.session_state.state["first_part_visible"] = False
        st.rerun()
