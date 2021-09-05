# #猜拳
# import random
# a=int(input('请输入石头剪刀布（0,1,2）'))
# b=random.randint(0,2)
# print('你输入了',a)
# print('电脑输入了',b)
# if (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
#     print('你赢了')
# elif a==b:
#     print('平局了')
# else:
#     print('你输了')

# 一到一百之和
# s=1
# sum=0
# while s<101:
#     sum=sum+s
#     s=s+1
#     print(sum)
# print(sum)
#
# s=0

#一到一百之和2
# for i in range(1,101):
#     s=s+i
# print(s)

#99乘法口诀表
# n=1
# m=1
# s=0
# while s<9:
#     while m<=n:
#         print(m, '*', n, '=', n * m,' ',end='')
#         m = m + 1
#     print('')
#     n=n+1
#     s=s+1
#     m=1

#根据输入百分制的成绩打印及格或不及格
# s=int(input('请输入成绩'))
# if 0<=s<60:
#     print('不及格')
# elif s>60:
#     print('及格了')

#统计100以内个位数是2并且能被3整除的数的个数
# s=0
# sum=0
# while s<=100:
#     if s%10==2:
#         sum=sum+1
#     s=s+1
# print(sum)

# 输入一个正整数，求它是几位数
# s=int(input('请输入一个正整数'))
# # x=0
# # while True:
# #     x=x+1
# #     if s//10**x==0:
# #         break
# # print(x)
# 输入一个正整数，求它是几位数2
# s=input('请输入一个整数')
# x=len(s)
# print(x)

# s = ('按时发发发啊.mp4')
# a = s.rpartition('.')
# print(a[2],r"\n",sep='')
# print(s.rindex('发'))
# print(s.replace("发", "fa"))


# def test():
#     import random
#     a = input('请输入石头(0)剪刀(1)布(2),输入exit退出')
#     if a.upper()==("EXIT"):
#         return ("")
#     b = random.randint(0, 2)
#     if a.isdigit():
#         a=int(a)
#         for i in range(0,3):
#             if i==a:
#                 break
#             elif i!=2:
#                 continue
#             else:
#                 print("输入错误,请重新输入")
#                 return test()
#         c = ["石头", "剪刀", "布"]
#         print('你出了', c[a], sep="")
#         print('电脑出了', c[b], sep="")
#         if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
#             print("你赢了")
#         elif a == b:
#             print("平局")
#         else:
#             print("你输了")
#     else:
#         print("输入错误，请重新输入")
#         return test()
#     return YN()
#
# def YN():
#     s=input("再来一局？输入Y/N")
#     if s.upper()=="Y":
#         print(test())
#     elif s.upper()=="N":
#         exit()
#     else:
#         print("请输入Y/N")
#         print(YN())
# print(test())

#石头剪刀布游戏
def test():
    import random
    a = input('请输入石头(0)剪刀(1)布(2),输入exit退出')
    if a.upper()==("EXIT"):
        exit()
    b = random.randint(0, 2)
    if a.isdigit():
        a=int(a)
        if a in [0,1,2]:
            c = ["石头", "剪刀", "布"]
            print('你出了', c[a], sep="")
            print('电脑出了', c[b], sep="")
            if (a<b) or (a == 2 and b == 0):
                print("你赢了")
            elif a == b:
                print("平局")
            else:
                print("你输了")
        else:
            print("输入错误,请重新输入")
            return test()
    else:
        print("输入错误，请重新输入")
        return test()
    YN()
# 再来一局
def YN():
    s=input("再来一局？输入Y/N")
    if s.upper()=="Y":
        print(test())
    elif s.upper()=="N":
        exit()
    else:
        print("请输入Y/N")
        print(YN())
print(test())
