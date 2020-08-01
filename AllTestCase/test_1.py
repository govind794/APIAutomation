import requests
import json

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

response = requests.get(url)
assert response.status_code == 200

# Response data is null
if response == None:
    print("Response data is null.")
else:
    json_response = json.loads(response.text)["list"]  # list assign value in the json_response

    # Loop Iterate all list value
    array_list = []
    for i in range(len(json_response)):
        days = json_response[i]['dt_txt'][8:10]  # days value get and assign through slicing
        array_list.append(days)

    data_set = sorted(set(array_list))
    count = 0
    for j in range(len(data_set)):
        for k in range(len(json_response)):
            if count <= 3:
                if list(data_set)[count] == json_response[k]['dt_txt'][8:10]:
                    print(json_response)
                    assert True
        count += 1
