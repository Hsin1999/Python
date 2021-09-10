import os
from datetime import datetime
#获取现在的时间：string（年-月-日 时：分：秒）
def time_Now():
    return datetime.now().strftime('%y-%m-%d')

#获取主目录绝对路径
def main_Path():
    return os.path.split(os.path.abspath(__file__))
def request_param():
        pass
def read_Config():
    return time_Now()


print(read_Config())