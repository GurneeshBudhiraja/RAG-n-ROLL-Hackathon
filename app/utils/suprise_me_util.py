from dotenv import load_dotenv
import random
from snowflake.cortex import Complete
from app.utils.snowflake_utils import create_snowflake_connection
import re, json

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
            "mistral-large2",  # Model used for suprise me content
            f"Tell me something informative about farming that could help educate the farmers in developing countries.It needs to be informative content related to the {topic} useful for farmers which could enhance the knowledge of the farmers in the {lang} ONLY. At the end return a short heading and short content which is no longer than 2 sentences in the following JSON format: {{'heading':'<model heading response>','content':'<model content response>'}}. Do not add any other text in the response apart from what has been mentioned above.",
        )
        modified_model_response = extract_heading_and_content(model_response.strip())
        return modified_model_response

    except Exception as e:
        print("Error:", e)
        return {"heading": "", "content": ""}


def extract_heading_and_content(response_text):
    """
    Extracts the 'heading' and 'content' values from a string, handling various formatting cases.
    """
    # Try extracting JSON directly if the response is valid JSON
    try:
        data = json.loads(response_text)
        if "heading" in data and "content" in data:
            return {
                "heading": data.get("heading", "").strip(),
                "content": data.get("content", "").strip(),
            }
    except json.JSONDecodeError:
        pass  # Continue with regex if JSON decoding fails

    # Handle potential JSON-like structure but as plain text
    json_like_pattern = r"\{.*?['\"]heading['\"]\s*:\s*['\"](.*?)['\"],\s*['\"]content['\"]\s*:\s*['\"](.*?)['\"]\s*}"
    match = re.search(json_like_pattern, response_text, re.DOTALL)
    if match:
        heading = match.group(1).strip()
        content = match.group(2).strip()
        return {"heading": heading, "content": content}

    # Handle less structured cases (e.g., plain text with keywords)
    plain_text_pattern = r"heading[:=]\s*(.*?)[\n,;]+.*?content[:=]\s*(.*?)[\n,;]+"
    match = re.search(plain_text_pattern, response_text, re.DOTALL | re.IGNORECASE)
    if match:
        heading = match.group(1).strip()
        content = match.group(2).strip()
        return {"heading": heading, "content": content}

    # Return empty values if no match is found
    return {"heading": "", "content": ""}


if __name__ == "__main__":
    topic = get_random_topic(topics=topics)
    print("Topic:", topic)

    model_response = get_surprise_content(lang="English", topic=topic)
    print("Model Response:", model_response)
