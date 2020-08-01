import requests
import json
import pytest




@pytest.yield_fixture()
def api_response():
    print("\n-----------SignUp By Email Test Case-----------")
    url = 'https://feature3.drivezytest.com/user'
    file = open('/Users/govind794/Documents/GitHub/APIAutomation/Resources/signup.json', 'r')
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


def test_signUpByEmail(api_response_body_json):
    user_details = api_response_body_json["response"]
    email = user_details['email']
    print(f'\n Email id: {email}')
    # assert 'MP70N20180008564' == email
