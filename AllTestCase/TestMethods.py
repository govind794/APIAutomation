import pytest
import requests
import json
import re


class TestMethods():
    @pytest.yield_fixture()
    def setUp(self):
        self.url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
        response = requests.get(self.url)

        # Response data is null
        if response == None:
            print("Response data is null.")

        self.json_response = json.loads(response.text)["list"]  # list assign value in the json_response

        # List data is empty
        if self.json_response == None:
            print("Response list data is null.")

        yield
        print("<---------Completed Test Case--------->")


# def test_1(self, setUp):
#     # Loop Iterate all list value
#     array_list = []
#     for i in range(len(self.json_response)):
#         days = self.json_response[i]['dt_txt'][8:10]  # days value get and assign through slicing
#         array_list.append(days)
#
#     data_set = sorted(set(array_list))
#     count = 0
#     for j in range(len(data_set)):
#         for k in range(len(self.json_response)):
#             if count <= 3:
#                 if list(data_set)[count] == self.json_response[k]['dt_txt'][8:10]:
#                     print(self.json_response)
#                     assert True
#         count += 1
#
# def test_2(self):
#     # Loop Iterate all list value
#     for i in range(len(self.json_response)):
#         times = self.json_response[i]['dt_txt'][11:13]  # times value get and assign through slicing
#         if int(times) != None:  # Data check for days
#             assert True
#         else:
#             assert False
#
# def test_3(self):
#     # temp value not be assign global level so I am assuming main temp less then equel to and greater then equel to
#     for i in range(len((self.json_response))):
#         response = self.json_response[i]['main']  # main data assign
#
#         min = response['temp_min']  # assign temp min value
#         max = response['temp_max']  # assign temp max value
#         temp = response['temp']  # assign temp value
#
#         if temp >= min and temp <= max:  # condition true check min and max
#             assert True
#         else:
#             assert False
#
# def test_4(self):
#     # Loop Iterate all list value
#     for i in range(len(self.json_response)):
#         weather_data = self.json_response[i]['weather'][0]  # weather object value assign in weather_data
#
#         if weather_data['id'] == 500:  # Confition check weather
#             print(weather_data['description'])
#             msg = weather_data['description']
#             assert re.match(r'light rain', msg)  # Assert re module through match string value

    def test_5(self, setUp):
        # Loop Iterate all list value
        for i in range(len(self.json_response)):
            weather_data = self.json_response[i]['weather'][0]  # weather object value assign in weather_data

            if weather_data['id'] == 800:  # Confition check weather
                print(weather_data['description'])
                msg = weather_data['description']
                assert re.match(r'clear sky', msg)  # Assert re module through match string value

# if __name__ == '__main__':
#     unittest.main()
