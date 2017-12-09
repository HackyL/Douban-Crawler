import requests
import tkinter
from lxml import etree


a=[]             #URL
name=[]      #电影名
director=[]  #导演
country=[]   #制片国家
date=[]        #上映日
pnum=[]      #评价人数
actor=[]      #主演
score=[]      #评分
content=[]
k=0

def get_image(t,num):
    img=requests.get(t)
    with open('%d.jpg'%num,'wb') as fp:
        fp.write(img.content)

for j in range(0,10): 
    url='https://movie.douban.com/top250?start={}&filter='.format(j*25) 
    html=requests.get(url).content
    root=etree.HTML(html)
    for i in root.xpath('//div[@class="info"]'):
        title=i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
        aum=i.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        bum=i.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
        if aum>='8' and bum<='150000人评价':
            ur0= i.xpath('div[@class="hd"]/a/@href')
            a.append(ur0[0])
            k+=1
            name.append(title)
            score.append(aum)
            pnum.append(bum)
            #print(title)
            #print(a[k])
            #print('Top %d'%k)
            #print('影片名称：%s\n'%title,'评分：%s '%aum,' %s'%bum )


for j in range(0,k):
    print('正在爬取第 %d 部电影数据'%(j+1))
    url=a[j]
    html=requests.get(url).content
    root=etree.HTML(html)
    t=root.xpath('normalize-space(//title/text())')
    print(t)
    if t=='页面不存在':
        continue
    for i in root.xpath('//div[@id="info"]'):
        t=i.xpath('span[1]/span[@class="attrs"]/a/text()')        #导演
        director.append(t)
        t=[i.xpath('span[@class="actor"]/span[@class="attrs"]/a[1]/text()'),i.xpath('span[@class="actor"]/span[@class="attrs"]/a[2]/text()')]    #主演
        actor.append(t)
        t=i.xpath('span[@property="v:initialReleaseDate"]/text()')     #上映日期
        date.append(t)
    t=root.xpath('normalize-space(//span[@property="v:summary"]/text())')    #内容简介
    content.append(t)
    t=root.xpath('//div[@id="mainpic"]/a/img/@src')    #海报图片
    get_image(t[0],j+1)


fp=open('数据.txt','a+')
fp.truncate(0)
fp.close()
for i in range(0,k):
    fp=open('数据.txt','a+',encoding='utf-8')                   #这里必须要加  encoding='utf-8'，不然会因为编码问题报错
    pos1='No.%d'%(i+1)+'\n电影名：  %s'%name[i]+'\n导演：  %s'%director[i]+'\n主演：  %s'%actor[i]
    pos2='\n上映日期：  %s'%date[i]+'\n评分： %s'%score[i]+'\n评价人数： %s'%pnum[i]+'\n内容简介:%s'%content[i]
    fp.write(pos1)
    fp.write(pos2)
    fp.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    fp.close()
    print('No.',i+1)
    print('电影名：  ',name[i])
    print('导演：  ',director[i])
    print('主演：  ',actor[i])
    print('上映日期：  ',date[i])
    print('评分： ',score[i])
    print('评价人数： ',pnum[i])
    print('内容简介： ',content[i])

