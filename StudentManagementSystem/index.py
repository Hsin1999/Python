import json,csv,hmac,os,teacher_login
import random


def file_path(path,*filename):
    if path=='files':
        return os.path.join(os.path.abspath('.'), 'files', *filename[0])
    if path=='data':
        return os.path.join(os.path.abspath('.'),'data','teacher_data')
def start():#登录主界面
    while True:
        click=main()
        if click=='1':
            s=teacher_login.Teacher_Main()
        elif click=='2':
            register()
        elif click=='3':
            quit()
        else:
            print('请重新输入')

def main():#主界面文件读取
    try:
        with open(file_path('files',('main.txt',)), 'r', encoding='utf8') as f:
            concent=f.read()
            print(concent)
            print('请输入1-3：')
            click=input()
            return click
    except:
        raise print('error，message：未找到文件')

def data_teacher_read():#教师账号信息读取
    try:
        with open(file_path("data"),'r',encoding='utf8') as f:
            return json.loads(f.read())
    except:
        return {}
def data_teacher_write(data):#写入教师账号信息
    with open(file_path("data"), 'w', encoding='utf8') as f:
        f.write(json.dumps(data))
def sha(data):#sha256加密
    key=hmac.new(b'19990127','hsin'.encode('utf8'),digestmod='SHA256')
    s=hmac.new(key.hexdigest().encode('utf8'), data.encode('utf8'), digestmod='SHA256')
    return s.hexdigest()
def register():#注册账号
    while True:
        teacher_name=input('请输入账号（3-6位）：')
        if len(teacher_name)>=3 and len(teacher_name)<=6:
            for i in data_teacher_read().keys():
                if i == teacher_name:
                    print('账号重复')
                    break
            else:
                break
        else:
            print('账号长度不正确')
    while True:
        password=input('请输入密码（6-12位）：')
        if len(password)>=6 and len(password)<=12:
            break
        else:
            print('密码长度不正确')
    data_teacher=data_teacher_read()
    data_teacher[teacher_name]=sha(password)
    data_teacher_write(data_teacher)
    f=open(file_path('files',('*_student.csv'.replace('*',teacher_name),)) , 'w', encoding='utf8',newline='')
    ff=csv.writer(f)
    ff.writerow(['姓名','年龄'])
    f.close()

if __name__ == '__main__':
    start()