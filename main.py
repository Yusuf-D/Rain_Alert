import requests
from twilio.rest import Client

account_sid = "ACa4af4229630de5bde56d8fdef36e3e7e"
auth_token = "ffea79a6ad462e531d7110f87decdc16"

parameters = {
    "lat": 40.853271,
    "lon": 29.881519,
    "appid": "232401d9f0e4be3a87cca4591b428782",
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
        to="+905541510171", 
        from_="+12084860229",
        body="It's going to rain today. Remember to take an umbrella!")

    print(message.status)

