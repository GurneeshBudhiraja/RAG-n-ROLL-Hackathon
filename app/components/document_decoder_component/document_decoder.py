import streamlit as st
from app.components.document_decoder_component import first_part, second_part


def document_decoder(selected_language: str = "English"):
    # Initialize session state
    if "state" not in st.session_state:
        st.session_state.state = {
            "file_uploaded": False,
            "language_selected": False,
            "processing": False,
            "chat_ready": False,
            "messages": [
                {"role": "ai", "content": "This is the ai message"},
                {"role": "user", "content": "This is the user message"},
            ],
            "first_part_visible": True,
        }

    # Reset button
    if st.button("Reset"):
        st.session_state.state = {
            "file_uploaded": False,
            "language_selected": False,
            "processing": False,
            "chat_ready": False,
            "messages": [],
            "first_part_visible": True,
        }
        st.rerun()

    # App heading section
    st.title("Document Decoder 📄")
    st.text(
        "Upload your legal documents and get clear summaries and explanations in simple language."
    )

    # Step 1: File Upload and language selection
    if (
        not st.session_state.state["chat_ready"]
        and st.session_state.state["first_part_visible"]
    ):
        first_part.first_part()

    # Step 2: Chat interface for the user to query about the uploaded docs
    if (
        st.session_state.state["chat_ready"]
        and not st.session_state.state["first_part_visible"]
    ):
        second_part.second_part()


if __name__ == "__main__":
    document_decoder()
