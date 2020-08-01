import requests
import json
import re

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

response = requests.get(url)
assert response.status_code == 200

# Response data is null
if response == None:
    print("Response data is null.")
else:
    json_response = json.loads(response.text)["list"]  # list assign value in the json_response

    # Loop Iterate all list value
    for i in range(len(json_response)):
        if json_response[i] == None:
            print("Response list data is null")
        else:
            weather_data = json_response[i]['weather'][0]  # weather object value assign in weather_data
            if weather_data['id'] == 500:  # Confition check weather
                msg = weather_data['description']
                assert re.match(r'light rain', msg)  # Assert re module through match string value
