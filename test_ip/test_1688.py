#encoding=utf-8
#-*- coding:utf-8-*-
import os
import sys
sys.path.append('/tools/python_common')
from common_func import *
import requests
from requests_toolbelt.adapters.source import SourceAddressAdapter
from lxml import etree
import subprocess
import re

URL_STR = 'https://detail.1688.com/offer/546403378656.html'
DIR_PATH = sys.path[0] + '/'
LOG_FILE = DIR_PATH + 'spider.log'
RESULT_FILE = DIR_PATH + 'result.txt'
USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36'
headers = {
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
# 'cookie':'_uab_collina=150018711483600631244249; JSESSIONID=c84Z1oi-IFxXGEN7ouozKBNzb8-M40KWPQ-8a43; cookie2=16421c84ab4be372b98ef56aacf745ee; t=3fbb79e703859df218741014c6a4a4ee; _tb_token_=c1be610706f3e; __cn_logon__=false; cna=sPfxEX5viykCAXtnT9zPPeC4; UM_distinctid=15d4a1eb5ca182-0ec3f1fc357506-333f5902-1fa400-15d4a1eb5cb5bf; _csrf_token=1500187117162; alicnweb=touch_tb_at%3D1500187116403; CNZZDATA1253659577=1784888096-1500183862-%7C1500183862; _tmp_ck_0="repzlpczqMsvs8UgT1IRFNnR2W%2BbDUo%2F0FRhBmEFXEAeQ3BKkTKPoXflfeRbT66Y1o2KeOiHxigxQ6fuXpy3cbFHaUmnH4VBoCnqwCNMHk9HyEsebX4yZ1G3NkEzfRzisLZOQsWSKY63%2BJ1%2FWZ9KFqJMEtnd7nn1Z3XzJcdWTNQe6xAhxHnmxnGxOHYTDX8oXcWRDQvlQ%2B9o8%2BsneaCKBO%2Bm4dfnELuN1%2Fs66DSaS0fU6W0YXDYaHD%2FxN9xbaZ0fUqybuHQS2jVU37wXbcycStbPGfIgKEuXBQohKiCCz5tHiy%2F6ef%2BFp%2BNcVVwDYHNDeET1gnKy37MX6EpqIrz2Z9BMYtyQOD1b2Nhx54az%2BUTk1EcpGZEepsCr%2FFWS7BnxHi4Zj%2FgaGTc%3D"; isg=AlJSCSVOX4ap86N6RbQWKSOYoxj0y3Tx-A53FhyrfoXwL_IpBfOmDVhF673o; _umdata=85957DF9A4B3B3E83F0C3136C9BF48408EFB1460E4160FEC38F1171381A11CAC89FF173889271F72CD43AD3E795C914C51B66B0E20BE166A9935E24B666B807C',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

ip_list = get_ip_list_from_locale()
print len(ip_list)

useful_ips = []
for ip in ip_list:
    s = requests.Session()
    s.mount('http://', SourceAddressAdapter((ip, 0)))
    s.mount('https://', SourceAddressAdapter((ip, 0)))
    # headers = {'User-Agent':USERAGENT}
    errmsg = ''
    try:
        r = s.get(URL_STR, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            if r.text.find('3828520321_1658767953') > 0:
                print '[SUCCEED] %s len=%d' %(ip, len(r.text))
                useful_ips.append(ip)
                continue
    except Exception, e:
        errmsg = str(e)

    print '[FAILED] %s code=%d redirect=%s errmsg=%s' %(ip, r.status_code, r.headers.get('Location', ''), errmsg)


print 'useful ip:%d' %(len(useful_ips))
print str(useful_ips)
