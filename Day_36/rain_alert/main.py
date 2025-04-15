#------------------------------------------------ Raining alert ------------------------------------------- #
# this python code will send an SMS message to warn him if it is raining or not 
import requests
from twilio.rest import Client

#The coming data is not real so it will not work
api_key = "6366457be73723c2898544asdfFA"
acc_sid = "ACj21312ASFfaAVAerGlE1312Fa123Af"
auth_token = "05145FvaFkjAkf9123FkiE12DASk234"

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_prams = {
    "lat":30.560598,
    "lon":31.010904,
    "appid":api_key,
    "cnt":4
}
response = requests.get(OWM_EndPoint, params=weather_prams)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    Condition_code = int(hour_data["weather"][0]["id"])
    if Condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(acc_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today. remember to bring an umbrella !",
        from_="+15215169866",
        to="+15245779544"
    )

