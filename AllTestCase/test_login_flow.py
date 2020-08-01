import requests
import json
import re

url = "https://feature3.drivezytest.com/login"

file = open("/File/param.json", 'r')
json_input = file.read()

post_response = requests.post(url, json.loads(json_input))
request_response = json.loads(post_response.text)

assert post_response.status_code == 200

if request_response["success"] == True:
    response = request_response["response"]
    assert request_response["success"] == True
    assert response["email"] == "govind.patidar@drivezy.com"
    try:
        assert request_response["success"] == True
        assert response["email"] == "govind.patidar@drivezy.com"
        msg = [response["first_name"], response["last_name"]]
        assert re.match(r'Govind', msg[0])
        assert re.match(r'Patidar', msg[1])
        print("-----Success TestCase-----")
    except:
        print("-----Failed TestCase-----")
        raise AssertionError("Does not match")
