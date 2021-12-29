import requests
from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

parameters = {
    "lat": YOUR_LATITUDE,
    "lon": YOUR_LONGITUDE,
    "appid": "YOUR_APP_ID",
    "exclude": "current,daily,minutely"
}

respond = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
respond.raise_for_status()

data = respond.json()
will_rain = False

for i in range(12):
    if data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="YOUR_PHONE_NUMBER", 
        from_="YOUR_TWILIO_ACCOUNT_PHONE_NUMBER",
        body="It's going to rain today. Remember to take an umbrella!")

    print(message.status)

