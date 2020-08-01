import pytest


class Test():
    @pytest.yield_fixture()
    def setUp(cls):
        print("\nOpen url to login")
        yield
        print("\nCloseing browser after login")

    def test_loginByEmail(setUp):
        print("Login by email")

    def test_loginByFacebook(setUp):
        print("Login by facebook")


if __name__ == '__main__':
    pytest.main()