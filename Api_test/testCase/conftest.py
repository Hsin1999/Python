import pytest,requests,mysql
@pytest.fixture()
def sql():
    db=mysql.Database('47.101.53.77','root','ppaa1122','test')
    return db