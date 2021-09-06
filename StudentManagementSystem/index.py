import json
import login
import csv
import hmac
import os

file=os.path.abspath('.')+'\\files\\'
teacher_data=os.path.abspath('.')+r'\data\teacher_data'
def start():#登录主界面
    while True:
        click=main()
        if click=='1':
            login.login()
        elif click=='2':
            register()
        elif click=='3':
            quit()
        else:
            print('请重新输入')

def main():#主界面文件读取
    try:
        with open(file+'main.txt', 'r', encoding='utf8') as f:
            concent=f.read()
            print(concent,'\n请输入1-3：')
            click=input()
            return click
    except:
        print('error，message：未找到文件')
        print(file + 'main.txt')
        return quit()

def data_teacher_read():#教师账号信息读取
    try:
        with open(teacher_data,'r',encoding='utf8') as f:
            return json.loads(f.read())
    except:
        return {}
def data_teacher_write(data):#写入教师账号信息
    with open(teacher_data, 'w', encoding='utf8') as f:
        f.write(json.dumps(data))
def sha(data):#sha256加密
    s=hmac.new(b'hsin', data.encode('utf8'), digestmod='SHA256')
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
    f=open(file + '*_student.csv'.replace('*',teacher_name), 'w', encoding='utf8',newline='')
    ff=csv.writer(f)
    ff.writerow(['姓名','年龄'])
    f.close()

if __name__ == '__main__':
    start()