import requests
import json
import pytest


@pytest.yield_fixture()
def api_response():
    # url = Global.baseUrl + "/" + API.login
    print("\n-----------Login By Gmail Test Case-----------")
    url = 'https://feature3.drivezytest.com/authGoogle'
    file = open('/Users/govind794/Documents/GitHub/APIAutomation/Resources/google_token.json', 'r')
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


def test_loginByGmail(api_response_body_json):
    license_details = api_response_body_json["response"]
    license_number = license_details['license_number']
    is_license_validated = license_details['is_license_validated']
    print(f'\n license_number: {license_number} \n is_license_validated: {is_license_validated}')
    assert 'MP70N20180008564' == license_number
    assert 1 == is_license_validated
