import pytest


test_user_data=[{"user":"admin1","psw":"1111"}]

@pytest.mark.parametrize("login", test_user_data, indirect=True)
def get_token(login):
    a=login

if __name__ == '__main__':
    pytest.main(["-s","TestClass.py"])


if __name__ == "__main__":
    pytest.main(["-s", "test_03.py"])
