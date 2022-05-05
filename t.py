# import time
#
# def hello():
#     time.sleep(1)
#
# def run():
#     for i in range(5):
#         hello()
#         print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！
# if __name__ == '__main__':
#     run()
# import time
# import asyncio
#
# # 定义异步函数
# async def hello():
#     print('Hello World:%s' % time.time())
#     print('Hello World1:%s' % time.time())
#
# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())
#
# loop = asyncio.get_event_loop()
# if __name__ =='__main__':
#     run()
# def coroutine_example(name):
#     print('start coroutine...name:', name)
#     x = yield name #调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
#     print('send值:', x)
#     return 'zhihuID: Zarten'
#
# def grouper2():
#     result2 = yield from coroutine_example('Zarten') #在此处暂停，等待子生成器的返回后继续往下执行
#     print('result2的值：', result2)
#     return result2
#
# def grouper():
#     result = yield from grouper2() #在此处暂停，等待子生成器的返回后继续往下执行
#     print('result的值：', result)
#     return result
#
# def main():
#     g = grouper()
#     next(g)
#     print("我继续执行了")
#     try:
#         g.send(10)
#     except StopIteration as e:
#         print('返回值：', e.value)
#
# if __name__ == '__main__':
#     main()
# import asyncio
# def my_callback(future):
#     print('返回值：', future.result())
# async def coroutine_example():
#     await asyncio.sleep(5)
#     return 'result'
# loop = asyncio.get_event_loop()
# coro = coroutine_example()
# task=loop.create_task(coro)
# print("等待请求回来")
# task.add_done_callback(my_callback)
# loop.run_until_complete(coro)
# loop.close()
# import asyncio
# import threading

# import mysql
# loop=asyncio.get_event_loop()
# async def a():
#     return 123
# async def select():
#     s = mysql.Database('47.101.53.77', 'root', 'ppaa1122', 'test')
#     task=await s.select_Mysql('select * from t_student',1)
#
# loop.run_until_complete(select())
# import threading
# import asyncio
# async def xc():
#     print('12321313123')
# async def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     r=await xc()
#     await asyncio.sleep(2)
#     print('Hello again! (%s)' % threading.currentThread())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()
# import asyncio
# import time
# async def a(x):
#     await asyncio.sleep(x)
#     print('我在运行a%s'%x)
# async def b(x):
#     await asyncio.sleep(x)
#     print('我在运行b%s'%x)
# async def main():
#     n=time.time()
#     task=asyncio.create_task(a(2))
#     results=await asyncio.gather(a(1),b(5),a(3),a(4),a(5),task)
#     s=time.time()-n
#     return s
# print(asyncio.run(main()))
# import asyncio
# from datetime import datetime
#
# import aiohttp
# from lxml import etree
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
#                          "/537.36 (KHTML, like Gecko) "
#                          "Chrome/72.0.3626.121 Safari/537.36"}
#
#
# async def get_movie_url():
#     req_url = "https://movie.douban.com/chart"
#     async with aiohttp.ClientSession(headers=headers) as session:
#         async with session.get(url=req_url, headers=headers) as response:
#             result = await response.text()
#             result = etree.HTML(result)
#             print(result.xpath("//*[@id='content']/div/div[1]/div/div/table/tr/td/a/@href"))
#         return result.xpath("//*[@id='content']/div/div[1]/div/div/table/tr/td/a/@href")
#
#
# async def get_movie_content(movie_url):
#     async with aiohttp.ClientSession(headers=headers) as session:
#         async with session.get(url=movie_url, headers=headers) as response:
#             result = await response.text()
#             result = etree.HTML(result)
#         movie = dict()
#         name = result.xpath('//*[@id="content"]/h1/span[1]//text()')
#         author = result.xpath('//*[@id="info"]/span[1]/span[2]//text()')
#         movie["name"] = name
#         movie["author"] = author
#     return movie
#
# if __name__ == '__main__':
#     start = datetime.now()
#     loop = asyncio.get_event_loop()
#     movie_url_list = loop.run_until_complete(get_movie_url())
#     tasks = [get_movie_content(url) for url in movie_url_list]
#     movies = loop.run_until_complete(asyncio.gather(*tasks))
#     print(movies)
#     print("异步用时为：{}".format(datetime.now() - start))
# import yaml
# y='''
# name: 回来
# age: 0
# job: 12
# '''
# y=yaml.unsafe_load(y)
# with open('api/testcase.yaml', 'r') as f:
#     s=yaml.unsafe_load(f)
# print(y)
# print(s)
# import threading
# s=2
# lock=threading.Lock()
# def run(n):
#     global s
#     for i in range(1,n):
#         lock.acquire()
#         s*=s
#         print(s)
#         lock.release()
# def run1(n):
#     global s
#     for i in range(1,n):
#         lock.acquire()
#         s/=s
#         print(s)
#         lock.release()
# a=threading.Thread(target=run,args=(100,))
# b=threading.Thread(target=run1,args=(100,))
# a.start()
# b.start()
# a.join()
# b.join()
# from collections import deque
# a=deque()
# a.append('1')
# a.append('1')
# a.append('1')
# a.append('1')
# a.appendleft('2')
# a.pop()
# print(a)
# import random, time, queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
#
# # 接收结果的队列:
# result_queue = queue.Queue()
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
# def task_quque():
#     task_queue = queue.Queue()
#     return task_queue
# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue',task_queue())
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import random,time,queue
# from multiprocessing.managers import BaseManager
# #发送任务队列
# task_queue=queue.Queue()
# #接收结果队列
# result_queue=queue.Queue()
#
# #继承BaseManager
# class QueueManager(BaseManager):
#     pass
# def return_task_queue():
#     #global 用于函数内部，修改全局变量的值
#     global task_queue
#     return task_queue
# def return_result_queue():
#     global result_queue
#     return result_queue
# if __name__=='__main__':
#     #将两个Queue注册到网络上，callable参数关联Queue对象
#     #！win10中callale不对lambda匿名函数做处理
#     QueueManager.register('get_task_queue',callable=return_task_queue)
#     QueueManager.register('get_result_queue',callable=return_result_queue)
#     #绑定端口5000，这5000怎么来的？两个文件中的端口一样就行！，设置验证码abc
#     #通过QueueManager将Queue暴露出去
#     manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
#     manager.start()
#     task=manager.get_task_queue()
#     result=manager.get_result_queue()
#     #放10个任务进去
#     for i in range(10):
#         n=random.randint(0,1000)
#         print('Put task %d...'%n)
#         #将数据放到任务队列
#         task.put(n)
#     #取任务执行结果
#     print('Try get results...')
#     for i in range(10):
#         #从结果队列中取结果
#         #等待10是因为计算需要时间
#         r=result.get(timeout=10)
#         print('REsult:%s'%r)
#     #关闭
#     manager.shutdown()
#     print('master end')
# import openpyxl
# f=openpyxl.open('1.xlsx')
# sheet=f.worksheets[0]
# f.create_named_range('qwe',sheet)
# import os
# def path():
#     return os.path.abspath(__file__)

# l1 = [ 'b' , 'c' , 'd' , 'b' , 'c' , 'a' , 'a' ]
# a=set(l1)
# a=list(a)
# print(a)
# s=sorted(a)
# print(s)
import logging
import re
import time
from logging.handlers import RotatingFileHandler
# logger = logging.getLogger()  # 日志器名称默认为root
# logger1 = logging.getLogger()  # 日志器名称默认为root
#
# # 设置两个处理器handler
# console_handler = logging.StreamHandler()
# console_handler1 = logging.StreamHandler()
#
# # 给两个相同名称的logger添加上处理器
# logger.addHandler(console_handler)
# logger1.addHandler(console_handler1)
#
# # 设置一下格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s')
# console_handler.setFormatter(formatter)
# console_handler1.setFormatter(formatter)
#
# # 输出日志记录
# logger1.warning("输出一条日志记录")
# class Log:
#     logger=logging.getLogger('logger')
#     logger1=logging.getLogger('logger.qq')
#     logger1.propagate=True
#     logger.setLevel(logging.INFO)
#     formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     formatter1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     console=logging.StreamHandler()
#     file=logging.handlers.RotatingFileHandler(filename='4.log',encoding='utf8',maxBytes=1024,backupCount=2)
#     file.setLevel(logging.INFO)
#     console.setFormatter(formatter)
#     file.setFormatter(formatter1)
#     logger.addHandler(console)
#     logger.addHandler(file)
#     logger1.info('12313')
#     logger.info('www')
# Log()
# import re
# a=re.compile('^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
# aaa=a.match('18525358730@163.com')
# print(aaa.group(0))
#
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# ll=sorted(L,key=lambda x:[x[1],x[0].lower()],reverse=True)
# print(ll)
# print(ord('我'))
# print('\u4e2d\u6587')
# print(int('1000',base=10))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print(f'hello,world{time.strftime("%Y-%m-%d %H:%M:%S")}')
# import hmac
# a=hmac.new(key=b'www',msg=b'wqwe',digestmod='SHA1')
# print(int(a.hexdigest(),base=16))
# s={}
# s[a.hexdigest()]=1
# print(s)
# import time
# start= time.time()
# for i in range(0,1001):
#     for j in range(0,1001):
#         for k in range(0,1001):
#             if i+j+k==1000 and i**2+j**2==k**2:
#                 print(i,j,k)
# end = time.time()
# print("总开销：",end-start)#总开销： 126.49699997901917
#
# start1= time.time()
# for i in range(0,1001):
#     for j in range(0,1001):
#         k=1000-i-j
#         if i**2+j**2==k**2:
#             print(i,j,k)
# end1= time.time()
# print("总开销：",end1-start1)#总开销： 1.0120000839233398
# print(bin(1111))
# print(hex(123456))
# print(oct(111))

# class SingleNode(object):
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
#     def __call__(self, *args, **kwargs):
#         print('111')
# s=Student()
# s.birth=1
# print(s._birth)
# print(s.age)
# print(s)
# s()
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
# a=Chain()
# s=a.qq.qw.er
# print(a)
# print(s)
# from dataclasses import dataclass
# @dataclass
# class Car:
#     color:str
#     mileage:float
#     automatic:bool
# car1=Car('red',3100.9,True)
# print(car1)
# from collections import namedtuple
# Car=namedtuple('Car','color mileage automatic')
# car1=Car('red',100.9,True)
# print(car1)
# from queue import Queue
# import threading
# q=Queue()
# lock=threading.Lock()
# data=threading.local
# s=10000
# def c(time):
#     global s
#     for i in range(time):
#         lock.acquire()
#         s-=100
#         print(s)
#         lock.release()
# def d(time):
#     global s
#     for i in range(time):
#         lock.acquire()
#         s += 100
#         print(s)
#         lock.release()
#
# def main():
#     cc=threading.Thread(target=c,args=(100000,))
#     dd=threading.Thread(target=d,args=(100000,))
#     cc.start()
#     dd.start()
#     cc.join()
#     dd.join()
#     print(s)
# main()
# def aa(q,data):
#     global r
#     for i in range(1,101):
#         # lock.acquire()
#         r*=100
#         q.put(i*r/data)
#         data+=1
#         # lock.release()
#     print('线程1%d'%data)
# def bb(q,data):
#
#     global r
#     for i in range(1,101):
#         # lock.acquire()
#         r/=100
#         qq=q.get()
#         print(qq * i*r/data)
#         data += 1
#         # lock.release()
#     print('r=%d'%r)
#     print('线程2%d' % data)
# def main():
#     data=0
#     a=threading.Thread(target=aa,args=(q,data))
#     b=threading.Thread(target=bb,args=(q,data))
#     a.start()
#     b.start()
#     a.join()
#     b.join()
# main()
from bs4 import BeautifulSoup
# import requests
# import re,csv
# response=requests.request('get','https://www.baidu.com',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
# page=response.content
# print(page)
# bs=BeautifulSoup(page,'html.parser')
# # print(bs)
# bss=bs.find_all('img')
# print(bss)
# print(bs.select('a>p'))
# for i in bss:
#     print(i)
#     print("")
# print(bss)
# goodsname=re.compile(r'<p class="name">(.*?)</p>')
# goodsid=re.compile(r'/goods/detail/(.*?);')
# goodsdiscount=re.compile(r'<p class="discount">(.*?)</p>')
# goodsprice=re.compile(r'<p class="item_price">(.*?)</p>')
# a=goodsid.findall(str(bss))
# # a=[i for i in a if len(str(a))!=0]
# b=goodsname.findall(str(bss))
# # b=[i for i in b if len(str(a))!=0]
# c=goodsdiscount.findall(str(bss))
# # c=[i for i in c if len(str(a))!=0]
# d=goodsprice.findall(str(bss))
# # d=[i for i in d if len(str(a))!=0]
# print(a,b,c,d)
# with open('goods.csv','w',newline='',encoding='utf8') as f:
#     ff=csv.writer(f)
#     for i in range(len(a)):
#         ff.writerow([a[i],b[i],c[i],d[i]])
# from lxml import etree
# html = '<html><body><h1>This is <a>a</a> test</h1></body></html>'
# # 将html转换成_Element对象
# _element = etree.HTML(html)
# # 通过xpath表达式获取h1标签中的文本
# text = _element.xpath('//h1')
# print(text)
# a=etree.tostring(text[0],method='text')
# print(a.decode('utf8'))
import mysql
s = mysql.Database('47.101.53.77', 'root', 'ppaa1122', 'diaoxiaoyi')
print(s.select_Mysql('select * from tblStudent'))