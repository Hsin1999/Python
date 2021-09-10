import pytest,requests,mysql
#开启数据库实例
@pytest.fixture()
def sql():
    db=mysql.Database('47.101.53.77','root','ppaa1122','test')
    return db