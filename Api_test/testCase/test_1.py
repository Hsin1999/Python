import requests,os,log
import config
def test_baidu1(sql):
    response=requests.request('get','http://www.baidu.com')
    response.encoding='utf8'
    select=sql.select_Mysql('select * from t_student',1)
    print(select)
    log.write_Log(response.url)
def test_baidu2(sql):
    response=requests.request('get','http://www.baidu.com')
    response.encoding='utf8'
    select=sql.select_Mysql('select * from t_student',1)
    print(select)
    log.write_Log(response.url)

def test_baidu3(sql):
    response = requests.request('get', 'http://www.baidu.com')
    response.encoding = 'utf8'
    select = sql.select_Mysql('select * from t_student', 1)
    print(select)
    log.write_Log(response.url)
def test_baidu4(sql):
    response=requests.request('get','http://www.baidu.com')
    response.encoding='utf8'
    select=sql.select_Mysql('select * from t_student',1)
    print(select)
    log.write_Log(response.url)