import time,os,pytest,config
from datetime import datetime
if __name__ == '__main__':
    #测试报告保存在report/xx、捕获系统日志
    pytest.main(['-vs','--html='+os.path.join(os.path.abspath('.'),'report',config.read_Config()+'.html'),'--capture=sys'])