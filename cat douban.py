import requests,re,os
from bs4 import BeautifulSoup
response=requests.request('get','https://movie.douban.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
bs=BeautifulSoup(response.content,'html.parser')
bss=bs.body.find_all("img",src=re.compile("img"))
# print(bss)
rea=re.compile(r'src="(.*?)"')
a=[]
for i in bss:
    a.append(rea.findall(str(i))[0])
# print(a)
# print(os.path.realpath(__file__))
path=os.path.realpath(__file__)
# print(os.path.join(os.path.dirname(path),'photo'))
s=0
for i in a:
    s+=1
    response=requests.get(i)
    with open(os.path.join(os.path.join(os.path.dirname(path),'photo',str(s)+r".jpg")),'wb') as b:
        b.write(response.content)