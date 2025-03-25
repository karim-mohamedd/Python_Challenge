# sunset and sunrise
import requests
from datetime import datetime
# The lat and long of egypt
MY_LAT = 26.820553
MY_LONG = 30.802498

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}
# I am passing parameters in form of dictionary
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sun_rise = data["results"]["sunrise"]
sun_set = data["results"]["sunset"]
day_length = data["results"]["day_length"]

print(f"The sun rise in Egypt is: {sun_rise} and the sunset is: {sun_set} the day length is: {day_length}")

