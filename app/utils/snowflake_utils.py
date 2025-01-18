import snowflake.connector
from dotenv import load_dotenv
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session
from snowflake.core import Root
import os

load_dotenv()


def create_snowflake_connection(database: str, cortex_search_service: str):
    try:
        # Checks and returns an active session
        active_session = get_active_session()
        if active_session:
            root = Root(active_session)
            svc = (
                root.databases[database]
                .schemas["DATA"]
                .cortex_search_services[cortex_search_service]
            )
            return svc

    except Exception as e:
        # Creates and returns a new session
        connection_object = snowflake.connector.connect(
            user=os.environ.get("SNOWFLAKE_USER"),
            password=os.environ.get("SNOWFLAKE_PASSWORD"),
            account=os.environ.get("SNOWFLAKE_ACCOUNT"),
            warehouse=os.environ.get("WAREHOUSE"),
            database=database,
            schema=os.environ.get("SCHEMA"),
        )
        # Create a Snowpark session from the connection
        active_session = Session.builder.configs(
            {"connection": connection_object}
        ).create()
        root = Root(active_session)

        svc = (
            root.databases[database]
            .schemas["DATA"]
            .cortex_search_services[cortex_search_service]
        )
        return svc


def get_similar_chunks_search_service(
    user_question, question_category, svc, columns, limit
):
    filter_obj = {
        "@eq": {"category": question_category},
    }
    response = svc.search(user_question, columns, filter=filter_obj, limit=limit)
    return (response).model_dump_json()
