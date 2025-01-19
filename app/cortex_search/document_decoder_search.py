from snowflake.cortex import Complete
from app.utils.snowflake_utils import create_snowflake_connection
from app.utils.snowflake_utils import get_similar_chunks_search_service
from snowflake.cortex import Complete

COLUMNS = ["chunk_text"]


# number of chunks
NUM_CHUNKS = 5


# Database name
DATABASE = "DOCUMENT_DECODER"


def document_decoder_search(
    user_question, selected_langauge, cortex_search_service, chat_history=[]
):
    try:
        svc = create_snowflake_connection(
            database=DATABASE, cortex_search_service=cortex_search_service
        )
        user_query = user_question

        if chat_history:
            user_query = generate_user_query(
                user_question=user_question, chat_history=chat_history
            )

        chunk_data = get_similar_chunks_search_service(
            user_question=user_query,
            svc=svc,
            columns=COLUMNS,
            limit=NUM_CHUNKS,
        )
        print("Chunk data: ")
        print(chunk_data)

        prompt = f"""
        You will act as a helpful assistant that will answer the user_question based on the provided data. If the answer is not there in the provided data politely decline the request. 
        
        The answer should be natural and based on the user_question needs, the answer could be long or short. Do not add a follow up question in the answer. Only provide the answer to the user_question.I have also provided you the chat_history of the current conversation for you to get an idea what is the context of the conversation. The user wants the answer in the {selected_langauge}. Do not answer anything outside of the chat history or data provided. If the information is not in the data reply positively how you can not answer that question due to the missing of data. Also, depending on the question requirements and needs the answer could be long or short accordingly. Since this section is for educating the farmers make sure to tailor the reponses accordingly. 
        
        FYI: The empty array in the chat_history means it is empty. 
        
        <chat_history>
        {chat_history}
        </chat_history>  

        DO NOT ADD ANY TEXT IN THE ANSWER. ONLY GIVE THE ANSWER IRRESPECTIVE OF THE LANGUAGE. I DO NOT NEED ANY TAGS AT THE START OR AT THE END OF THE ANSWER. AT LAST, REPLY THE USER IN {selected_langauge} ONLY IRRESPECTIVE OF THE USER_QUESTION LANGUAGE AND DATA LANGUAGE. 

        <user_question>
          {user_query}
        </user_question>

        <data>
          {chunk_data}
        </data>
        """

        print("Getting model response")
        model_response = Complete("mistral-large", prompt)
        return model_response
    except Exception as e:
        print(e)
        return ""


def generate_user_query(user_question, chat_history=[]):
    prompt = f"""
        Below is the user_question:
        <user_question>
        {user_question}
        </user_question>
        
        Below is the chat_history of the conversation (FYI: if the chat_history is considered empty if chat_history is []):
        <chat_history>
        {chat_history}
        </chat_history>

        I want you understand the context of the conversation using the chat_history and understand the user_question and then generate a completed user question so that the new question covers all the aspects and meaning of the original question. Do not mention any other text in the response except from the new generated query. DO NOT MENTION WORDS LIKE chat_history, user_question in the final response. Only the new generated query should be returned. Do not elaborate the question provided only mention in the final question what has been initially asked by the user.
      """
    model_response = Complete("mistral-large", prompt)
    return model_response


def get_similar_chunks_search_service(user_question, svc, columns, limit):
    filter_obj = {}
    response = svc.search(user_question, columns, filter=filter_obj, limit=limit)
    return (response).model_dump_json()


if __name__ == "__main__":
    model_response = document_decoder_search(
        user_question="Are there any government incentives/schemes related to organic farming",
        question_category="Government Schemes",
        selected_langauge="English",
        chat_history=[],
    )

    print(model_response)
