import pytest,config
#参数化test
@pytest.mark.parametrize('method,url,status_code',config.params())
def test_all(url,method,status_code):
    r=config.Request(method,url)
    response=r.get_response()
    r.encoding='utf8'
    # 断言状态码==200
    assert response.status_code==status_code
