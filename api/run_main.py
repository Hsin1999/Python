import pytest,os,config




if __name__ == '__main__':
    pytest.main(['-vs','--html='+os.path.join(os.path.abspath('.'),'report',config.read_Config()+'.html'),'--capture=sys'])