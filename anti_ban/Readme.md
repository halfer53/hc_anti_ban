#背景
---------------------

为了防止抓取被封禁IP，以及方便调整不同域名的抓取间隔时间，编写了通用的scrapy中间件。以后只要在setting.py中配置即可。

#中间件
---------------------
##下载中间件：自动切换天津代理IP或本机IP
downloadmiddleware/anti_ban.py

**配置：**
```
DOWNLOADER_MIDDLEWARES = {
   'alad_offline.downloadmiddleware.anti_ban.AntiBanMiddleware': 543,
}
 
SPIDER_INFO = {
    'ID': 'TJ_01',  # 天津抓取机1~7分别对应TJ_01~TJ_07（如果设置了MULTI_IP[MONGO] == True，则会根据该ID在mongo中搜索对应的IP）
    'SUB_ID': 0,    # 暂未使用，可用于自定义分布式抓取
    'SUB_NUM': 7,   # 暂未使用，可用于自定义分布式抓取
    'TJ_PROXY': False,  # 是否使用天津抓取及的代理IP，如果设置为True，则MULTI_IP不生效
    'PUB_PROXY': False, # 暂未使用
    'MULTI_IP': {'MONGO': False,    # 是否从mongo读取ID对应的IP地址
                 'LOCALE_ALL': False,   # 是否使用本机的所有IP地址
                 'LOCALE_ONE': False,   # 是否只用本机默认的一个IP地址
                 'NEED_AUTH': False}    # 是否在初始化时对所有IP进行验证
}
```
##延时中间件：根据不同的域名设置不同的延时
extensions/AutoThrottleWithList.py

**配置：**
```
AUTOTHROTTLE_ENABLED = True
 
EXTENSIONS = {
            'alad_offline.extensions.AutoThrottleWithList.AutoThrottleWithList':300,
            }
 
LIMIT_SITES = (
    {'ID': 'WEB', 'REGEX': r'.*\/page\/creditdetail.htm$', 'DEALY_TIME': 10},
    {'ID': 'BAIDU_LINK', 'REGEX': r'.*www\.baidu\.com\/link.*', 'DEALY_TIME': 1},
)
```
**PS：由于延时会阻塞整个抓取流程，所以对抓取效率要求较高的项目，推荐根据延时需求分成几个小的scrapy程序**

##其他防止ban的方法
**设置useragent**
```
USER_AGENT = 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'      # 百度spider
 
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'    # 浏览器
```

#源码
---------------------
mabosen@210.82.113.17:~/GIT/anti_ban.git

#测试用例
 ---------------------
mabosen@210.82.113.17:~/GIT/alad_offline.git   baidu_company
天津第一台：/app/baidu_company
