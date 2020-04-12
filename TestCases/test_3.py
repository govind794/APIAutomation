import requests
import json

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

response = requests.get(url)

# response data is empty
if response == None:
    print("Response data is null.")
else:
    json_response = json.loads(response.text)["list"]

    for i in range(len(json_response)):

        # List data is empty
        if json_response == None:
            print("Response data is null.")
        else:
            for i in range(len((json_response))):
                response = json_response[i]['main']  # main data assign

                min = response['temp_min']  # assign temp min value
                max = response['temp_max']  # assign temp max value
                temp = response['temp']  # assign temp value

                if temp > min and temp < max:  # condition true check min and max

                    days = json_response[i]['dt_txt'][8:10]  # days value get and assign
                    if int(days) < 31:  # 4 days print value
                        assert True
                else:
                    print('No data found.')  # condition false case
                    assert False
