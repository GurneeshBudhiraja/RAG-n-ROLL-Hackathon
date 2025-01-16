import os
from mistralai import Mistral
from dotenv import load_dotenv
import json
import random

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

        topic = get_random_topic(topics=topics)

        api_key = os.environ["MISTRAL_API_KEY"]
        model = "mistral-large-2407"

        # Creates mistral client
        client = Mistral(
            api_key=api_key,
        )

        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me something informative about farming that could help educate the farmers in developing countries.It needs to be informative content related to the {topic} useful for farmers which could enhance the knowledge of the farmers in the following {lang}. At the end return a short heading and short content which is no longer than 2 sentences in the following JSON format: {{'heading':'<model heading response>','content':'<model content response>'}}",
                },
            ],
            temperature=1,
            random_seed=10000,
            response_format={
                "type": "json_object",
            },
        )

        # Converts the chat_response from JSON to Python dict
        model_response = json.loads(chat_response.choices[0].message.content)
        return model_response
    except Exception as e:
        print("Error:", e)
        return {"heading": "", "content": ""}


if __name__ == "__main__":
    topic = get_random_topic(topics=topics)
    print("Topic:", topic)

    model_response = get_surprise_content(lang="English", topic=topic)
    print("Model Response:", model_response)
