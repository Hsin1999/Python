import csv

import requests,re,os
from bs4 import BeautifulSoup
path=os.path.realpath(__file__)
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
response=requests.request('get','https://movie.douban.com/',headers=header)
bs=BeautifulSoup(response.content,'html.parser')
bss=bs.body.find_all(class_="poster")
# print(bss)
rea=re.compile(r'src="(.*?)"')
alt=re.compile(r'alt="(.*?)"')
href=re.compile(r'href="(.*?)"')
a=[]
b=[]
c=[]
for i in bss:#获取所有链接到列表
    a.append(rea.findall(str(i))[0])
for i in bss:
    b.append(alt.findall(str(i))[0])
for i in bss:
    c.append(href.findall(str(i))[0])
for i in range(len(b)):#写入数据到photo/电影列表.csv文件中
    with open(os.path.join(os.path.join(os.path.dirname(path),'photo',r"电影列表.csv")),'a',newline='',encoding='utf8') as f:
        ff=csv.writer(f)
        ff.writerow([b[i],c[i]])
s=0
for i in a:#下载图片文件到photo/
    s+=1
    response=requests.get(i)
    with open(os.path.join(os.path.join(os.path.dirname(path),'photo',str(s)+r".jpg")),'wb') as b:
        b.write(response.content)
