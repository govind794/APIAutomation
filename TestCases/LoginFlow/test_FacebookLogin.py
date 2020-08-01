import requests
import json
import pytest


@pytest.yield_fixture()
def api_response():
    print("\n-----------Login By Facebook Test Case-----------")
    url = 'https://feature3.drivezytest.com/authFacebook'
    file = open('/Users/govind794/Documents/GitHub/APIAutomation/Resources/facebook_token.json.json', 'r')
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


def test_loginByFacebook(api_response_body_json):
    print("\n-----------Login By Facebook Test Case-----------")
    license_details = api_response_body_json["response"]
    license_number = license_details['license_number']
    is_license_validated = license_details['is_license_validated']
    print(f'\n license_number: {license_number} \n is_license_validated: {is_license_validated}')
    assert 'MP70N20180008564' == license_number
    assert 1 == is_license_validated
