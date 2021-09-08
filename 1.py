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
def coroutine_example(name):
    print('start coroutine...name:', name)
    x = yield name #调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
    print('send值:', x)
    return 'zhihuID: Zarten'

def grouper2():
    result2 = yield from coroutine_example('Zarten') #在此处暂停，等待子生成器的返回后继续往下执行
    print('result2的值：', result2)
    return result2

def grouper():
    result = yield from grouper2() #在此处暂停，等待子生成器的返回后继续往下执行
    print('result的值：', result)
    return result

def main():
    g = grouper()
    next(g)
    print("我继续执行了")
    try:
        g.send(10)
    except StopIteration as e:
        print('返回值：', e.value)

if __name__ == '__main__':
    main()
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
import threading

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
