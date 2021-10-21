import requests,re,os,csv,asyncio,time
from bs4 import BeautifulSoup
t=time.time()
path=os.path.realpath(__file__)
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
response=requests.request('get','https://movie.douban.com/',headers=header)
bs=BeautifulSoup(response.content,'html.parser')
bss=bs.body.find_all(class_="poster")
# print(bss)
rea=re.compile(r'src="(.*?)"')
alt=re.compile(r'alt="(.*?)"')
href=re.compile(r'href="(.*?)"')
a,b,c=[],[],[]
s=0
for i in bss:#获取所有链接到列表
    a.append(rea.findall(str(i))[0])
for i in bss:
    b.append(alt.findall(str(i))[0])
for i in bss:
    c.append(href.findall(str(i))[0])
async def save():
    print('开始保存电影标题和链接')
    with open(os.path.join(os.path.join(os.path.dirname(path), 'photo', r"电影列表.csv")), 'a', newline='',encoding='utf8') as f:
        for i in range(len(b)):#写入数据到photo/电影列表.csv文件中
            ff=csv.writer(f)
            ff.writerow([b[i],c[i]])
            print(f'电影：{b[i]}信息保存完成')
async def download(a):# 下载图片文件到photo/
    print('开始下载图片')
    global s
    tasks=[]
    photos=[]
    for i in a: #请求图片源码
        photos.append(asyncio.create_task(get_photo(i)))
    await asyncio.wait(photos)
    for j in photos:#将图片保存到本地
        s+=1
        tasks.append(asyncio.create_task(download1(s,j.result())))
    await asyncio.wait(tasks)
async def get_photo(i):
    return requests.get(i)
async def download1(s,origin):
    with open(os.path.join(os.path.join(os.path.dirname(path), 'photo', str(s) + r".jpg")), 'wb') as b:
        b.write(origin.content)
        print(f'下载图片{s}完成')
async def main():
    task1=asyncio.create_task(save())
    task2=asyncio.create_task(download(a))
    await asyncio.gather(task1,task2)
    y=time.time()-t
    print('耗时%d'%y)
asyncio.run(main())

# import csv,time
#
# import requests, re, os
# from bs4 import BeautifulSoup
# t=time.time()
# path = os.path.realpath(__file__)
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
# response = requests.request('get', 'https://movie.douban.com/', headers=header)
# bs = BeautifulSoup(response.content, 'html.parser')
# bss = bs.body.find_all(class_="poster")
# # print(bss)
# rea = re.compile(r'src="(.*?)"')
# alt = re.compile(r'alt="(.*?)"')
# href = re.compile(r'href="(.*?)"')
# a = []
# b = []
# c = []
# for i in bss:  # 获取所有链接到列表
#     a.append(rea.findall(str(i))[0])
# for i in bss:
#     b.append(alt.findall(str(i))[0])
# for i in bss:
#     c.append(href.findall(str(i))[0])
# for i in range(len(b)):  # 写入数据到photo/电影列表.csv文件中
#     with open(os.path.join(os.path.join(os.path.dirname(path), 'photo', r"电影列表.csv")), 'a', newline='',
#               encoding='utf8') as f:
#         ff = csv.writer(f)
#         ff.writerow([b[i], c[i]])
# s = 0
# for i in a:  # 下载图片文件到photo/
#     s += 1
#     response = requests.get(i)
#     with open(os.path.join(os.path.join(os.path.dirname(path), 'photo', str(s) + r".jpg")), 'wb') as b:
#         b.write(response.content)
# y=time.time()-t
# print('耗时%d'%y)