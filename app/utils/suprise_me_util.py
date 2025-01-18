from dotenv import load_dotenv
import random
from snowflake.cortex import Complete
from app.utils.snowflake_utils import create_snowflake_connection
import re


load_dotenv()

# Topics regarding farming
topics = [
    "SoilHealth",
    "CropRotation",
    "PestControl",
    "Fertilization",
    "Irrigation",
    "WeedControl",
    "PrecisionAgriculture",
    "FarmManagementSoftware",
    "WeatherData",
    "RenewableEnergy",
    "MarketPrices",
    "FinancialPlanning",
    "MarketingStrategies",
    "FoodSafety",
    "ClimateChange",
    "ConservationAgriculture",
    "Biodiversity",
    "WaterQuality",
    "LivestockNutrition",
    "AnimalHealth",
    "AnimalWelfare",
]


def get_random_topic(topics, num_shuffles=10):
    """
    Gets the random topic from the topics list
    """
    shuffled_topics = topics.copy()
    for _ in range(num_shuffles):
        random.shuffle(shuffled_topics)
    return random.choice(shuffled_topics)


def get_surprise_content(lang: str):
    """
    This function is used to get the random content about farming from the Mistral AI model
    """
    try:
        create_snowflake_connection(
            database="INFORMATION_ACCESS",
            cortex_search_service="INFORMATION_ACCESS_SEARCH_SERVICE_CS",
        )
        topic = get_random_topic(topics=topics)

        model_response = Complete(
            "mistral-7b",  # Model used for suprise me content
            f"Tell me something informative about farming that could help educate the farmers in developing countries.It needs to be informative content related to the {topic} useful for farmers which could enhance the knowledge of the farmers in the following {lang}. At the end return a short heading and short content which is no longer than 2 sentences in the following JSON format: {{'heading':'<model heading response>','content':'<model content response>'}}",
        )
        modified_model_response = extract_heading_and_content(model_response)
        return modified_model_response

    except Exception as e:
        print("Error:", e)
        return {"heading": "", "content": ""}


import re


def extract_heading_and_content(text):
    """
    Extracts the 'heading' and 'content' values from a string using regular expressions.
    """
    pattern = r"{'heading':\s*'([^']*)',\s*'content':\s*'([^']*)'}"
    match = re.search(pattern, text)
    if match:
        heading = match.group(1)
        content = match.group(2)
        return {"heading": heading, "content": content}
    else:
        return {"heading": "", "content": ""}


if __name__ == "__main__":
    topic = get_random_topic(topics=topics)
    print("Topic:", topic)

    model_response = get_surprise_content(lang="English", topic=topic)
    print("Model Response:", model_response)
