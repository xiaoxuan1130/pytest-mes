#coding=utf-8
import pytest,requests,json


##获取app的authToken
@pytest.fixture(scope='session',autouse=True)
def loginApp(request):
    user = request.param["user"]
    psw = request.param["psw"]
    payload={"account":user,"password":psw}
    url = "http://192.168.3.166:8280/member/v1/user/login/password"
    r=requests.post(url,data=payload)
    authTokenText=r.text
    contentJson=json.loads(authTokenText);
    authToken =contentJson.get("b").get("authToken");
    return exchangeToken(authToken)



def exchangeToken(authToken):
    url="http://192.168.3.171:8880/webapi/v1/app/apply_token"
    payload={"auth_token":authToken}
    r=requests.post(url,data=payload)
    tokenText=r.text
    contentJson=json.loads(tokenText)
    token=contentJson.get("b").get("token")
    return token





