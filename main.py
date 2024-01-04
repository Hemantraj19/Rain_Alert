import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(".venv/.env")

API_KEY = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 23.344101,
    "lon": 85.309563,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_codes = [weather_data['list'][i]['weather'][0]['id'] for i in range(4)]
will_rain = True if any(code < 700 for code in weather_codes) else False

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today🌧️",
        from_='number_you_got_from_twilio',
        to='your_phone_number'
    )

    print(message.status)
