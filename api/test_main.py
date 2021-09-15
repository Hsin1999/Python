import pytest,requests,config
#参数化test
@pytest.mark.parametrize('method,url,status_code',config.params())
def test_all(url,method,status_code):
    response=requests.request(method,url=url)
    response.encoding='utf8'
    # 断言状态码==200
    assert response.status_code==status_code
if __name__ == '__main__':
    pytest.main()