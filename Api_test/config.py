import os
from datetime import datetime
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


print(read_Config())