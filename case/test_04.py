#coding=utf-8
import pytest,requests,json

test_user_data = [{"user": "13857600211", "psw": "123456"}]

@pytest.mark.parametrize("loginApp", test_user_data, indirect=True)
def test_getUser(loginApp):
    a=loginApp
    url="http://192.168.3.171:8880/webapi/v1/app/user_info"
    headers={"accessToken":a}
    r=requests.get(url,headers=headers)
    text=r.text
    contentJson=json.loads(text)
    content=contentJson.get("b")
    print(content)

def test_getCustomerPublic(loginApp):
    a=loginApp
    url = "http://192.168.3.171:8880/webapi/v1/common/customer_public/get"
    headers = {"accessToken": a}
    r = requests.get(url, headers=headers)
    text=r.text

def test_queryCustomer(loginApp):
    a = loginApp
    url = "http://192.168.3.171:8880/webapi/v1/customer/list?pageNo=1&pageSize=4"
    headers = {"accessToken": a}
    r = requests.get(url, headers=headers)
    text = r.text


if __name__ == '__main__':
    pytest.main("-s","test_04.py")