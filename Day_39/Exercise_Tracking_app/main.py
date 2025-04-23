
from dotenv import load_dotenv
import requests
import os
from datetime import datetime

# Dealing with nutritionix api
load_dotenv()

APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_params = {
    "query":input("What was your workout like today?: "),
    "weight_kg":float(input("What is your weight?: ")),
    "height_cm":float(input("What is your height?: ")),
    "age":int(input("How old are you?: ")),
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params ,headers=headers)
result = response.json()

print(result["exercises"])
# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Setting Google Sheets api 
GOOGLE_SHEET_NAME = "sheet1"
SHEET_ENDPOINT = os.environ["ENV_GOOGLE_SHEETS_ENDPOINT"]
SHEET_TOKEN = os.environ["ENV_GOOGLE_SHEETS_TOKEN"]

for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}
sheet_response = requests.post(url=SHEET_ENDPOINT,json=sheet_inputs, headers=bearer_headers)
data = sheet_response.json()
print(data)

