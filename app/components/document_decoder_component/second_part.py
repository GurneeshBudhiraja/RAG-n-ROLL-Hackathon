import streamlit as st
from app.cortex_search.document_decoder_search import document_decoder_search
from app.constants.document_decoder_constants import document_decoder_content


# Styles for the chat interface
def get_chat_style():
    return st.markdown(
        """
          <style>
              .stButton button {
                  transition: all 0.2s;
                  border: 1px solid #8ac774;
                  color: #8ac774;
                  font-weight: 500;
                  padding: 8px 16px;
                  border-radius: 6px;
                  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
              }
              .chat-container {
                  display: flex;
                  align-items: start;
                  margin-bottom: 16px;
                  color: black;
                  gap: 2px;
              }

              .chat-user {
                  justify-content: end;
                  flex-direction: row-reverse;
              }
              .chat-user > .chat-content {
                  background-color: #ff6c6c;
              }

              .chat-ai .chat-content {
                  justify-content: flex-start;
                  background-color: #ffbd44;
              }

              .chat-container > div:first-child {
                  margin-right: 8px;
                  font-size: 24px; /* Adjust emoji size */
                  display: flex;
                  align-items: center;
                  justify-content: center;
              }

              .chat-content {
                  background: #f7f9fa; /* Default background for user messages */
                  padding: 10px 16px;
                  border-radius: 8px;
                  max-width: 70%;
                  word-wrap: break-word;
              }

              

          </style>
          """,
        unsafe_allow_html=True,
    )


# Iterate on the messages list and show the past messages
def messages_util():
    messages = st.session_state.state["messages"]
    for message in messages:
        if message["role"] == "user":
            st.markdown(
                f"""
                <div class="chat-container chat-user">
                    <div>👨‍💻</div>
                    <div class="chat-content">{(message["content"])}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="chat-container chat-ai">
                    <div>🌾</div>
                    <div class="chat-content">{message["content"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def second_part(selected_language: str):
    get_chat_style()
    # Runs for the very first time
    if st.session_state.state["first_time"]:
        st.session_state.state["messages"].append(
            {
                "role": "ai",
                "content": document_decoder_content[selected_language][
                    "generating_summary"
                ],
            }
        )

        response_placeholder = st.empty()
        model_response = ""
        with st.spinner(document_decoder_content[selected_language]["summary_spinner"]):
            model_response = document_decoder_search(
                user_question="Generate a brief summary covering all the important aspects of the provided data.",
                chat_history=[],
                first_time=True,
                selected_langauge=st.session_state.state["language_selected"],
                cortex_search_service=f"{st.session_state.state['table_name']}_CS",
            )

        if model_response == "":
            model_response = document_decoder_content[selected_language][
                "unable_to_answer"
            ]
        st.session_state.state["messages"].append(
            {"role": "ai", "content": model_response}
        )
        response_placeholder.markdown(
            f"""
                <div class="chat-container chat-ai">
                    <div>🌾</div>
                    <div class="chat-content">{model_response}</div>
                </div>
            """,
            unsafe_allow_html=True,
        )
        st.session_state.state["first_time"] = False
    # Chat input
    user_query = st.chat_input(
        document_decoder_content[selected_language]["ask_question_placeholder"]
    )

    if user_query:
        # Appending the user message
        st.session_state.state["messages"].append(
            {"role": "user", "content": user_query}
        )

        messages_util()

        response_placeholder = st.empty()
        model_response = ""
        with st.spinner(
            document_decoder_content[selected_language]["generating_answer_spinner"]
        ):
            model_response = document_decoder_search(
                user_question=user_query,
                selected_langauge=st.session_state.state["language_selected"],
                chat_history=st.session_state.state["messages"],
                cortex_search_service=f"{st.session_state.state['table_name']}_CS",
            )
        if not model_response:
            st.error(document_decoder_content[selected_language]["unable_to_answer"])
            return
        st.session_state.state["messages"].append(
            {"role": "ai", "content": model_response}
        )
        response_placeholder.markdown(
            f"""
                <div class="chat-container chat-ai">
                    <div>🌾</div>
                    <div class="chat-content">{model_response}</div>
                </div>
            """,
            unsafe_allow_html=True,
        )
