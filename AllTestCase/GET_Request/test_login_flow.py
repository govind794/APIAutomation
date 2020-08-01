import requests
import json
import jsonpath

url = "https://secure.drivezytest.com/city?includes=venue"
# url = "https://feature3.drivezytest.com/login"

response = requests.get(url)

# print(response.content)
# print(response.headers)
print(response.status_code)
assert response.status_code == 200
print(response)
json_response = json.loads(response.text)["response"]

for i in range(len(json_response)):
    if json_response[i]["name"] == "Bengaluru":
        print("city_id =", json_response[i]["id"])
# print(json_response[i]["venue"])
# for j in range(len(json_response[2]["venue"])):
#     print(json_response[1]["venue"])

# path = jsonpath.jsonpath(json_response, "name")

# file = open("/Users/govind794/PycharmProjects/APIAutomation/File/param.json", 'r')
# json_input = file.read()
#
# post_response = requests.post(url, json.loads(json_input))
# request_response = json.loads(post_response.text)
#
# if request_response["success"] == True:
#     print(request_response["response"]["email"])


# def test_login_flow():
#     file = open("/Users/govind794/PycharmProjects/APIAutomation/File/param.json", 'r')
#     json_input = file.read()
#
#     post_response = requests.post(url, json.loads(json_input))
#     request_response = json.loads(post_response.text)
#
#     assert post_response.status_code == 200
#
#     if request_response["success"] == True:
#         print(request_response["response"]["email"])
#         assert request_response["success"] == True
#         assert request_response["response"]["email"] == "govind.patidar@drivezy.com"
