import unittest
import requests
import json

from Utility.Login.LoginFlow import loginFlow


class LoginTest(unittest.TestCase):
    def api_response():
        # url = Global.baseUrl + "/" + API.login
        print("\n-----------Login By Gmail Test Case-----------")
        url = 'https://feature3.drivezytest.com/login'
        file = open('/Users/govind794/Documents/GitHub/APIAutomation/Resources/google_token.json', 'r')
        json_input = file.read()
        return requests.post(url, json.loads(json_input))

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
        #     loginFlow(api_response_body_json)
        pass


# def test_loginByFacebook(self):
#     print("Login viwa facebook")
#     self.assertTrue(True)
#
# def test_loginByGmail(self):
#     print("Login viwa gmail")
#     self.assertTrue(True)

# @classmethod
# def tearDown(cls):
#     print("------Complete Login Test Case------")


if __name__ == '__main__':
    unittest.main()
