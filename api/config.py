import yaml,requests,os
from datetime import datetime
def params():#从yaml读取参数后，转换格式
    with open('testcase.yaml', 'r') as f:
        y = yaml.unsafe_load(f)
    l = []
    for i in y.values():
        l.append(tuple(i.values()))
    return l

#封装request方法
cookie=None
class Request():
    def __init__(self,mothod,url,header=None,params=None,body=None):
        self.mothod=mothod
        self.url=url
        self.header=header
        self.params=params
        self.body=body
        # if not cookie:
        #     self.cookie=Request.get_cookie(self)
    def get_cookie(self):
        response=requests.request(self.mothod,url=self.url,headers=self.header,params=self.params,data=self.body)
        return response.cookies
    def get_response(self):
        response=requests.request(self.mothod,url=self.url,headers=self.header,params=self.params,data=self.body)
        return response

#获取现在的时间：string（年-月-日）
def time_Now():
    return datetime.now().strftime('%y-%m-%d')

#获取主目录绝对路径or当前文件名 （func[0]or[1]）
def main_Path():
    return os.path.split(os.path.abspath(__file__))
def request_param():
        pass
def read_Config():
    return time_Now()
