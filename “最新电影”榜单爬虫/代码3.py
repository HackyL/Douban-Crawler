import requests
import tkinter
import time
from lxml import etree
from selenium import webdriver


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


def isElementExist(driver):
        flag=True
        try:
            driver.find_element_by_link_text('加载更多')
            return flag
        except:
            flag=False
            return flag


url='https://movie.douban.com/explore#!type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0'
#browser=webdriver.Chrome(executable_path='G:\\编程\\python\\chromedriver.exe')
browser=webdriver.PhantomJS(executable_path='G:\\编程\\python\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
browser.get(url)
time.sleep(1)
#browser.find_element_by_xpath('//div[@class="gaia"]/div[@class="list"]/a').click()
#browser.find_element_by_link_text('加载更多').click()

x=19
while x>=0:
    browser.find_element_by_link_text('加载更多').click()
    print('正在加载第%d页'%(20-x))
    time.sleep(1)
    flag=True
    y=0
    while flag:
        try :
            browser.find_element_by_link_text('加载更多')
            flag=False
        except:
            print('未加载完，继续加载……')
            time.sleep(10)
            y+=1
            if y>=2:
                print('已加载完。')
                break
    x-=1
    if y>=2:
        break

html=browser.page_source
browser.quit()
#html1=requests.get(url).content
root=etree.HTML(html)
for i in root.xpath('//a[@class="item"]'):
    aum=i.xpath('p/strong/text()')[0]
    aum=str(aum)
    if aum>='7.5':
        ur=i.xpath('@href')[0]
        #print(ur)
        score.append(aum)
        a.append(ur)
        k+=1

print('开始爬取电影')
for j in range(0,k):
    print('正在爬取第 %d 部电影数据'%(j+1))
    url=a[j]
    html=requests.get(url).content
    root=etree.HTML(html)
    t=root.xpath('normalize-space(//title/text())')
    print(t)
    name.append(t)
    if t=='页面不存在':
        continue
    for i in root.xpath('//div[@id="info"]'):
        t=i.xpath('span[1]/span[@class="attrs"]/a/text()')        #导演
        director.append(t)
        t=i.xpath('text()[11]')            #制作国家
        country.append(t)
        t=[i.xpath('span[@class="actor"]/span[@class="attrs"]/a[1]/text()'),i.xpath('span[@class="actor"]/span[@class="attrs"]/a[2]/text()')]    #主演
        actor.append(t)
        t=i.xpath('span[@property="v:initialReleaseDate"]/text()')
        date.append(t)
    t=root.xpath('normalize-space(//span[@property="v:summary"]/text())')
    content.append(t)
    t=root.xpath('//div[@id="mainpic"]/a/img/@src')
    get_image(t[0],j+1)


fp=open('数据.txt','a+')
fp.truncate(0)
fp.close()
for i in range(0,k):
    fp=open('数据.txt','a+',encoding='utf-8')                   #这里必须要加  encoding='utf-8'，不然会因为编码问题报错
    pos1='No.%d'%(i+1)+'\n电影名：  %s'%name[i]+'\n导演：  %s'%director[i]+'\n主演：  %s'%actor[i]
    pos2='\n上映日期：  %s'%date[i]+'\n评分： %s'%score[i]+'\n内容简介:%s'%content[i]
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
    print('内容简介： ',content[i])





