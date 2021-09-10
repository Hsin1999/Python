import config,os
#日志写入log/xx
def write_Log(data):
    with open(os.path.join(config.main_Path()[0],'log',config.time_Now()),'a',encoding='utf8') as f:
        f.write(data+'\n')
