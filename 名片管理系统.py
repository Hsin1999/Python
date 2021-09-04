import time
data=[]
s=0
def main():
    a = '-'.center(20, '-')
    b = '名片管理系统'.center(14, ' ')
    c = '1:添加名片\n2:删除名片\n3:修改名片\n4:显示所有名片\n5:退出系统'
    print(a)
    print(b)
    print(c)
    print(a)
    x=input('')
    if x=='1':
        tj()
    elif x=='2':
        sc()
    elif x=='3':
        xg()
    elif x=='4':
        sy()
    elif x=='5':
        print('感谢使用')
        exit()
    else:
        main()
def xinxi(a):
    a['姓名']=input('请输入姓名')
    a['年龄']=input('请输入年龄')
    return a
def tj():
    a={}
    xinxi(a)
    data.append(a)
    print(data,'\n添加成功')
    time.sleep(1)
    main()
def sc():
    a={}
    xinxi(a)
    for i in data:
        if a==i:
            qw=data.index(i)
            data.pop(qw)
            print('删除成功')
            break
    else:
        print('信息错误')
    time.sleep(1)
    main()
def xg():
    a={}
    xinxi(a)
    for i in data:
        if a['姓名']==i['姓名'] and a['年龄']==i['年龄']:
            print('输入新的信息')
            a = {}
            xinxi(a)
            i['姓名']=a['姓名']
            i['年龄']=a['年龄']
            print(data)
    time.sleep(1)
    main()
def sy():
    print('姓名'.ljust(10, ' '), end='')
    print('年龄'.ljust(10, ' '))
    for i,j in enumerate(data):
        print(j['姓名'],''.ljust(8,' '),j['年龄'])
    time.sleep(1)
    main()
main()
