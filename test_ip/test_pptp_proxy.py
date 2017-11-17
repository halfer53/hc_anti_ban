#encoding=utf-8
#-*- coding:utf-8-*-
import os
import sys
import requests
sys.path.append('/tools/python_common')
from common_func import logInit
import logging
from time import sleep
from scrapy import Selector
import pdb

URL_STR = 'https://s.1688.com/company/company_search.htm?keywords=%B8%D6%B2%C4%D4%A4%B4%A6%C0%ED%CF%DF&button_click=top&earseDirect=false&n=y'
DIR_PATH = sys.path[0] + '/'
LOG_FILE = DIR_PATH + 'spider.log'
RESULT_FILE = DIR_PATH + 'result.txt'
USERAGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36'

def get_ip_by_proxy(ip, port, username='', password=''):
    if username and password:
        proxies = {
            "http": "http://%s:%s@%s:%s" % (username, password, ip, port),
            "https": "https://%s:%s@%s:%s" % (username, password, ip, port)
        }
    else:
        proxies = {
            "http": "http://%s:%s" % (ip, port),
            "https": "http://%s:%s" % (ip, port)
        }

    r = requests.get(URL_STR, proxies=proxies)
    if r.status_code == 200:
        #return r.text
		pdb.set_trace()
		sel = Selector(text = r.text)
		print sel.xpath('//div[@class="sw-mod-navigatebar fd-clr"]//li[@id="breadCrumbText"]/em/text()').extract()
    else:
        print r.status_code
        print proxies
        return ''


if __name__ == '__main__':
    logInit(logging.INFO, 'logs/test_pptp_proxy.log', 0, True)

    ip = '10.10.10.23'
    port = '8899'
    username = 'tj_user_3_1'
    password = '111111'
    if len(sys.argv) > 2:
        ip = sys.argv[1]
        port = sys.argv[2]
        if len(sys.argv) > 4:
            username = sys.argv[3]
            password = sys.argv[4]
        else:
            username = ''
            password = ''

    while True:
        ret = get_ip_by_proxy(ip, port, username, password)
        logging.info(ret.strip())
        sleep(1)
