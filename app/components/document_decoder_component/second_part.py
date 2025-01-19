import streamlit as st


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


def second_part():
    # Gets the chat styles
    get_chat_style()

    # Chat input
    user_query = st.chat_input("Ask a question about your documents...")

    if user_query:
        st.session_state.state["messages"].append(
            {"role": "user", "content": user_query}
        )

        messages_util()

        response_placeholder = st.empty()

        # TODO: testing model response
        model_response = "This is an interesting question. Let me help you with this!"

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
