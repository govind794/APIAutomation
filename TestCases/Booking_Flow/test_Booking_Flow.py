import requests
import json
import pytest

from Utility.Login.LoginFlow import loginFlow


@pytest.yield_fixture()
def api_response():
    print("\n-----------Login By Email Test Case-----------")
    url = 'https://feature3.drivezytest.com/login'
    file = open('/Users/govind794/Documents/GitHub/APIAutomation/Resources/login_param.json', 'r')
    json_input = file.read()
    return requests.post(url, json.loads(json_input))


@pytest.fixture()
def api_response_body_json(api_response):
    response = json.loads(api_response.text)
    if response["success"] == True:
        assert response["success"] == True
        return response
    else:
        raise AssertionError("API response:", response)


def test_status_code(api_response):
    if api_response.status_code == 200:
        print('status_code of response is:' + str(api_response.status_code))
        assert 200 == api_response.status_code
    else:
        raise AssertionError("API response:" + str(api_response.status_code))


def test_loginByEmail(api_response_body_json):
    loginFlow(api_response_body_json)
