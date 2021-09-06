import csv,index
# 学生信息增删改查
class Teacher_Main:
    def __init__(self):
        #登录界面
        self.__account_name = Teacher_Main.teacher_login(self)
        #教师主页面
        Teacher_Main.teacher_main(self)
    def teacher_login(self):
        data = index.data_teacher_read()
        while True:
            account = input('账号：')
            if account in data.keys():
                break
            else:
                print('账号不存在')
                return Teacher_Main.teacher_login(self)
        while True:
            password = input('密码：')
            if data[account] == index.sha(password):
                break
            else:
                print('密码错误，请重新输入')
                return Teacher_Main.teacher_login(self)
        return account
    def teacher_main(self):
        while True:
            Teacher_Main.performance(self)
            click = input('请输入数字')
            if click == '1':
                while True:
                    content = Teacher_Main.student_data_read(self)
                    student_name = input('请输入姓名：')
                    for i in content:
                        if i[0] == student_name:
                            print('姓名重复')
                            break
                    else:
                        break
                student_age = input('请输入年龄：')
                Teacher_Main.student_data_write(self, [student_name, student_age])
            elif click == '2':
                for i in Teacher_Main.student_data_read(self):
                    print(i)
            elif click == '3':
                Teacher_Main.student_data_update(self)
            elif click == '4':
                Teacher_Main.student_data_delete(self)
            elif click == '5':
                return index.start()
            else:
                print('请重新输入')

    def performance(self):  # 读取主界面2文件
        try:
            with open(index.file_path('files',('performance.txt',)), 'r', encoding='utf8') as f:
                print(f.read().replace('x', self.__account_name))
        except:
            print('error，message：未找到文件')
            return quit()
    # 教师账号下的学生信息读取
    def student_data_read(self):
        try:
            f = open(index.file_path('files',('*_student.csv'.replace('*', self.__account_name),)), 'r', encoding='utf8')
            ff = csv.reader(f)
            # 返回列表
            return ff
        except:
           raise print("学生信息文件缺失")

    # 写入教师账号下的学生信息，data：传列表，[学生姓名,年龄]
    def student_data_write(self, data):
        f = open(index.file_path('files',('*_student.csv'.replace('*', self.__account_name),)), 'a', encoding='utf8', newline='')
        ff = csv.writer(f)
        ff.writerow(data)
        f.close()

    # 更新学生信息
    def student_data_update(self):
        ff = Teacher_Main.student_data_read(self)
        s = []
        for i in ff:
            s.append(i)
        exit_flag = False
        while True:
            student_name = input('输入要修改的姓名')
            for i in s:
                if student_name == i[0]:
                    exit_flag = True
                    age = input('请输入要修改的年龄')
                    i[1] = age
                if exit_flag:
                    break
            if exit_flag:
                break
            else:
                print('查找不到信息')
        f = open(index.file_path('files',('*_student.csv'.replace('*', self.__account_name),)) , 'w', encoding='utf8', newline='')
        ff = csv.writer(f)
        ff.writerows(s)
        f.close()

    # 删除学生信息
    def student_data_delete(self):  # 删除学生信息
        ff = Teacher_Main.student_data_read(self)
        s = []
        for i in ff:
            s.append(i)
        exit_flag = False
        while True:
            student_name = input('请输入学生姓名')
            for i in s:
                if student_name == i[0]:
                    exit_flag = True
                    s.remove(i)
                    print('删除成功')
                    break
                if exit_flag:
                    break
            else:
                print('查找不到该学生信息')
            if exit_flag:
                break
        f = open(index.file_path('files',('*_student.csv'.replace('*', self.__account_name),)), 'w', encoding='utf8', newline='')
        ff = csv.writer(f)
        ff.writerows(s)
        f.close()