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
import asyncio
import time
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
import asyncio
from datetime import datetime

import aiohttp
from lxml import etree
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.121 Safari/537.36"}


async def get_movie_url():
    req_url = "https://movie.douban.com/chart"
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=req_url, headers=headers) as response:
            result = await response.text()
            result = etree.HTML(result)
            print(result.xpath("//*[@id='content']/div/div[1]/div/div/table/tr/td/a/@href"))
        return result.xpath("//*[@id='content']/div/div[1]/div/div/table/tr/td/a/@href")


async def get_movie_content(movie_url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=movie_url, headers=headers) as response:
            result = await response.text()
            result = etree.HTML(result)
        movie = dict()
        name = result.xpath('//*[@id="content"]/h1/span[1]//text()')
        author = result.xpath('//*[@id="info"]/span[1]/span[2]//text()')
        movie["name"] = name
        movie["author"] = author
    return movie

if __name__ == '__main__':
    start = datetime.now()
    loop = asyncio.get_event_loop()
    movie_url_list = loop.run_until_complete(get_movie_url())
    tasks = [get_movie_content(url) for url in movie_url_list]
    movies = loop.run_until_complete(asyncio.gather(*tasks))
    print(movies)
    print("异步用时为：{}".format(datetime.now() - start))