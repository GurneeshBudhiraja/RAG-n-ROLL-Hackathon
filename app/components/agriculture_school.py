import streamlit as st
from app.constants.agriculture_school_constants import agri_school_content
from app.utils.suprise_me_util import get_surprise_content
from app.cortex_search.agriculture_school_search import agriculture_school_search


def messages_util():
    messages = st.session_state["messages"]
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


def agriculture_school(selected_language):

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Gets the data for the selected language
    st.markdown(
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

    lang_content = agri_school_content[selected_language]

    # st.image("static/farmer_learning.jpg")
    st.header(lang_content["title"])

    st.write(lang_content["description"])  # Add the description back in

    user_question = st.chat_input(lang_content["input_placeholder"])

    # --- Surprise Me Button ---
    suprise_me_button = st.button(lang_content["surprise_me_button"])

    # --- Topic Selection ---
    st.markdown(lang_content["topic_selection_heading"])
    selected_topic = st.selectbox(
        lang_content["topic_selection_label"],
        lang_content["education_options"],
        index=None,
        placeholder=lang_content["topic_selection_placeholder"],
    )
    messages_util()
    if suprise_me_button:
        educational_content = get_surprise_content(lang_content)
        if not educational_content["heading"] or not educational_content["content"]:
            st.error(lang_content["model_response_error"])
            return
        st.markdown(f"#### {educational_content['heading'].strip()}")
        st.markdown(f"###### {educational_content['content'].strip()}")

    if user_question and not selected_topic:
        st.error(lang_content["error_message"])
    elif user_question and selected_topic:
        st.session_state.messages.append({"role": "user", "content": user_question})

        response_placeholder = st.empty()
        model_response = ""
        with st.spinner(lang_content["spinner_text"]):
            model_response = agriculture_school_search(
                user_question=user_question,
                question_category=selected_topic,
                selected_langauge=selected_language,
                chat_history=st.session_state.messages,
            )

        if not model_response:
            st.error(lang_content["model_response_error"])
        else:
            st.session_state.messages.append({"role": "ai", "content": model_response})
            response_placeholder.markdown(
                f"""
                    <div class="chat-container chat-ai">
                        <div>🌾</div>
                        <div class="chat-content">{model_response}</div>
                    </div>
                """,
                unsafe_allow_html=True,
            )

    return
