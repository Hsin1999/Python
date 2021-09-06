import index
import csv
import json
def login():#主界面2
    data=index.data_teacher_read()
    while True:
        account=input('账号：')
        if account in data.keys():
            break
        else:
            print('账号不存在')
    while True:
        password = input('密码：')
        if data[account] ==index.sha(password):
            break
        else:
            print('密码错误，请重新输入')
    while True:
        performance(account)
        click=input('请输入数字')
        if click=='1':
            a=[]
            while True:
                concent = student_data_read(account)
                student_name=input('请输入姓名：')
                for i in concent:
                    if i[0]==student_name:
                        print('姓名重复')
                        break
                else:
                    break
            sutdent_password=input('请输入年龄：')
            student_data_write(account,[student_name,sutdent_password])
        elif click=='2':
            for i in student_data_read(account):
                print(i)
        elif click=='3':
            student_data_update(account)
        elif click=='4':
            student_data_delete(account)
        elif click=='5':
            return index.start()
        else:
            print('请重新输入')


def student_data_read(name):#教师账号下的学生信息读取
    try:
        f=open(index.file+'*_student.csv'.replace('*',name),'r',encoding='utf8')
        ff=csv.reader(f)
        return ff
    except:
        print('读取不到学生信息')
        return quit()

def student_data_write(name,data):#写入教师账号下的学生信息
    f=open(index.file+'*_student.csv'.replace('*',name), 'a', encoding='utf8',newline='')
    ff=csv.writer(f)
    ff.writerow(data)
    f.close()

def student_data_update(name):#更改学生信息
    ff=student_data_read(name)
    s=[]
    for i in ff:
        s.append(i)
    exit_flag=False
    while True:
        student_name=input('输入要修改的姓名')
        for i in s:
            if student_name==i[0]:
                exit_flag = True
                age=input('请输入要修改的年龄')
                i[1]=age
            if exit_flag:
                break
        if exit_flag:
            break
        else:
            print('查找不到信息')
    print(s)
    f = open(index.file + '*_student.csv'.replace('*', name), 'w', encoding='utf8',newline='')
    ff = csv.writer(f)
    ff.writerows(s)
    f.close()
def student_data_delete(name):#删除学生信息
    ff=student_data_read(name)
    s = []
    for i in ff:
        s.append(i)
    exit_flag=False
    while True:
        student_name=input('请输入学生姓名')
        for i,j in enumerate(s):
            if student_name==j[0]:
                exit_flag=True
                s.pop(i)
                print('删除成功')
                break
            if exit_flag==True:
                break
        if exit_flag==True:
            break
        else:
            print('查找不到该学生信息')
    f = open(index.file + '*_student.csv'.replace('*', name), 'w', encoding='utf8',newline='')
    ff = csv.writer(f)
    ff.writerows(s)
    f.close()
def performance(name):#读取主界面2文件
        try:
            with open(index.file+'performance.txt','r',encoding='utf8') as f:
                print(f.read().replace('x',name))
        except:
            print('error，message：未找到文件')
            return quit()
