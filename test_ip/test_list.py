#encoding=utf-8
#-*- coding:utf-8-*-
import os
import sys
import requests
from requests_toolbelt.adapters.source import SourceAddressAdapter
from lxml import etree
import subprocess
import re

URL_STR = 'https://dexintianxia.1688.com/page/offerlist.htm'
DIR_PATH = sys.path[0] + '/'
LOG_FILE = DIR_PATH + 'spider.log'
RESULT_FILE = DIR_PATH + 'result.txt'
USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36'

def get_ip_list_from_locale():
    call_handle = subprocess.Popen('ifconfig',  shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ip_buf = call_handle.stdout.readlines()
    ip_list = re.findall(r'(?<=inet addr:)\d+\.\d+\.\d+\.\d+(?= )', str(ip_buf))
    ip_pub_list = []
    for ip in ip_list:
        if re.match(r'^1(((0|27)(.(([1-9]?|1[0-9])[0-9]|2([0-4][0-9]|5[0-5])))|(72.(1[6-9]|2[0-9]|3[01])|92.168))(.(([1-9]?|1[0-9])[0-9]|2([0-4][0-9]|5[0-5]))){2})$', ip):
            continue
        ip_pub_list.append(ip)
    return ip_pub_list


ip_list = get_ip_list_from_locale()
print len(ip_list)

useful_ips = []
for ip in ip_list:
    s = requests.Session()
    s.mount('http://', SourceAddressAdapter((ip, 0)))
    s.mount('https://', SourceAddressAdapter((ip, 0)))
    headers = {'User-Agent':USERAGENT}
    errmsg = ''
    try:
        r = s.get(URL_STR, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            response = etree.HTML(r.text)
            result = response.xpath("//ul[@class='offer-list-row']/li/div[@class='title']/a/@href")
            if result:
                print '[SUCCEED] %s len=%d' %(ip, len(r.text))
                useful_ips.append(ip)
                continue
    except Exception, e:
        errmsg = str(e)

    print '[FAILED] %s code=%d redirect=%s errmsg=%s' %(ip, r.status_code, r.headers.get('Location', ''), errmsg)
    

print 'useful ip:%d' %(len(useful_ips))
print str(useful_ips)

