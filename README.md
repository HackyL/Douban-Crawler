# Douban-Crawler

##### 这个项目是去年提交Python大作业时的结课项目。选题为:用Python爬取豆瓣冷门高分电影和书籍。
当时选择这个题目的初衷是为自己提供一个书籍电影的推荐渠道，因为相比那些热门火爆的书籍影视作品，自己更青睐于那些冷门小众精致的作品。

其实当时网络上关于豆瓣的爬虫已经很多了，甚至豆瓣都自己提供了API给大家。但是从学习技术的角度上考虑，还是决定自己能手动实践去爬。虽然这个项目难度不大，由于当时是初学者，而且并没有系统地学过爬虫相关知识，基本上一甩袖子就开始做，遇到问题基本都是Baidu/Google找资料解决，也踩了很多坑，因此整个过程还是比较曲折且有所收获的。

本次项目一共有四个爬虫，分别是用了四个不同的榜单，四个榜单分别是“豆瓣电影TOP250”，“豆瓣图书TOP250”，“最新电影”和“小说类图书”。
前两个榜单网页html的结构大致相似，也较为基础。“最新电影”榜单的网页html内容是动态获取的，“加载更多”也需要模拟网页动态点击。“小说类图书”的html结构和TOP250相似，但是数据量较大，爬虫爬取时极容易假死。然后把四个爬虫和项目报告整理后放在这里。

技术层面值得说的大概只有两点：一是模拟网页动态点击吧，采用了第三方模块Selenium和轻型浏览器PhantomJS的组合来用代码模拟浏览器点击操作。二是在充分了解正则表达式、Xpath和BeatifulSoup的优劣特点和基本操作后选择了Xpath来解析数据。

