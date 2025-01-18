from snowflake.cortex import Complete
from app.utils.snowflake_utils import create_snowflake_connection
from app.utils.snowflake_utils import get_similar_chunks_search_service

COLUMNS = ["chunk", "relative_path", "category"]

category_dict = {
    "Government Schemes": "government_schemes",
    "NGOs and Organizations": "ngos_and_organisations",
    "Helplines and Contacts": "helplines_and_contacts",
}

# number of chunks
NUM_CHUNKS = 5

# Search service name
CORTEX_SEARCH_SERVICE = "INFORMATION_ACCESS_SEARCH_SERVICE_CS"

# Database name
DATABASE = "INFORMATION_ACCESS"


def information_access_search(user_question, question_category, selected_langauge):
    try:
        svc = create_snowflake_connection(
            database=DATABASE, cortex_search_service=CORTEX_SEARCH_SERVICE
        )

        chunk_data = get_similar_chunks_search_service(
            user_question=user_question,
            question_category=category_dict[question_category],
            svc=svc,
            columns=COLUMNS,
            limit=NUM_CHUNKS,
        )

        prompt = f"""
        You will act as a helpful assistant that will answer the user_question based on the provided data. If the answer is not there in the provided data politely decline the request. 
        
        The answer should be natural and based on the user_question needs, the answer could be long or short. Do not add a follow up question in the answer. Only provide the answer to the user_question. The user has selected the category {question_category} and then asked the question.
        
        
        If the data that you got is not related to the question:
          1. Pick the most suitable category for the question from below: 
            <category>
            Government Schemes,
            NGOs and Organizations,
            Helplines and Contacts,
            </category>
          2. Then reply the user politely to select the appropriate category you selected
        

        DO NOT ADD ANY TEXT IN THE ANSWER. ONLY GIVE THE ANSWER IRRESPECTIVE OF THE LANGUAGE. I DO NOT NEED ANY TAGS AT THE START OR AT THE END OF THE ANSWER. AT LAST, REPLY THE USER IN {selected_langauge} ONLY IRRESPECTIVE OF THE USER_QUESTION LANGUAGE AND DATA LANGUAGE. 

        <user_question>
          {user_question}
        </user_question>

        <data>
          {chunk_data}
        </data>
        """

        model_response = Complete("mistral-large", prompt)
        return model_response
    except Exception as e:
        print(e)
        return ""


if __name__ == "__main__":
    model_response = information_access_search(
        user_question="Are there any government incentives/schemes related to organic farming",
        question_category="Government Schemes",
    )

    print(model_response)
