import requests
import json

url = "https://feature3.drivezytest.com/login"


def test_login_flow():
    file = open("/Users/govind794/PycharmProjects/APIAutomation/File/param.json", 'r')
    json_input = file.read()

    post_response = requests.post(url, json.loads(json_input))
    request_response = json.loads(post_response.text)

    assert post_response.status_code == 200

    if request_response["success"] == True:
        print(request_response["response"]["email"])
        assert request_response["success"] == True
        assert request_response["response"]["email"] == "govind.patidar@drivezy.com"
