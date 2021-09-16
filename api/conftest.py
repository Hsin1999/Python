import pytest
import requests
token=None

# @pytest.fixture(scope='session')

def set_up(token):
    if token:
        return token
    else:
        response=requests.request('get','http://uat-jobs.bilibili.com/api/auth/v1/csrf/token',headers={'X-AppKey':'ops.ehr-api.auth','X-UserType':'2'})
        return response

a=set_up(token)
print(a.text)
print(a.cookies)
