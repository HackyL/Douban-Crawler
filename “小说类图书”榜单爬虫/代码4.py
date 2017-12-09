import requests
import string
import re
import time
from lxml import etree

a2=[]             #URL
name2=[]      #书名
pnum2=[]      #评价人数
score2=[]      #评分
auther=[]       #作者
content=[]    #内容简介
k=0

def get_image(t,num):
    img=requests.get(t)
    with open('%d.jpg'%num,'wb') as fp:
        fp.write(img.content)

for i in range(0,20): 
    url='https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'.format(i*20)
    flag=True
    while flag:
        try:
            html=requests.get(url,timeout=5).content
            flag=False
        except:
            html=requests.get(url).content 
    root=etree.HTML(html)
    for i in root.xpath('//div[@class="info"]'):
        dnum=i.xpath('normalize-space(div[@class="star clearfix"]/span[@class="pl"]/text())')
        if dnum=='(少于10人评价)':
            continue
        cnum=i.xpath('div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
        if cnum[0]>='9':
            print('No.%d'%(k+1))
            topic=i.xpath('h2/a/@title')
            print(topic)
            ur=i.xpath('h2/a/@href')
            print(ur[0])
            a2.append(ur[0])
            name2.append(topic[0])
            pnum2.append(dnum)
            score2.append(cnum[0])
            k+=1

print('正在爬取%d本图书'%k)
for j in range(0,k):
    print('正在爬取第 %d 部图书数据'%(j+1))
    url=a2[j]
    flag=True
    num1=1
    while flag:
        try:
            html=requests.get(url,timeout=5).content
            flag=False
        except:
            num1+=1
    print('申请HTML共%d次。'%num1)
    root=etree.HTML(html)
    t=root.xpath('normalize-space(//title/text())')
    print(t)
    if t=='页面不存在':
        continue
    t=root.xpath('normalize-space(//div[@class="subject clearfix"]/div[@id="info"]/a[1]/text())')
    auther.append(t)
    t=root.xpath('normalize-space(//div[@class="intro"]/p/text())')
    content.append(t)
    t=root.xpath('//div[@id="mainpic"]/a/img/@src')    #海报图片
    get_image(t[0],j+1)


fp=open('数据.txt','a+')
fp.truncate(0)
fp.close()
for i in range(0,k):
    fp=open('数据.txt','a+',encoding='utf-8')
    pos='Top： %d'%(i+1)+'\n书名： %s'%name2[i]+'\n作者： %s'%auther[i]+'\n评分： %s'%score2[i]+'\n评价人数： %s'%pnum2[i]+'\n内容简介： %s'%content[i]
    fp.write(pos)
    fp.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    fp.close()
    print('No.',i+1)
    print('书名： ',name2[i])
    print('作者： ',auther[i])
    print('评分： ',score2[i])
    print('评价人数： ',pnum2[i])
    print('内容简介： ',content[i])




