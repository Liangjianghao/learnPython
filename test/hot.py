# -- coding: UTF-8 -- 
import sys
import os
import os.path
import urllib
import sys
import json
import requests
from lxml import html
from selenium import webdriver
import time

reload(sys)
sys.setdefaultencoding('utf8')
header_dict = {'Cookie':'ll="108296"; bid=qmAvaZ0e0TQ; ps=y; ct=y; _ga=GA1.2.1466963311.1510553394; _gid=GA1.2.603860126.1513085379; ue="1084933098@qq.com"; push_noty_num=0; push_doumail_num=0; as="https://movie.douban.com/explore"; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513088642%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=d7ee522b3ba2a991.1510553457.4.1513088642.1513085737.; __utma=30149280.1466963311.1510553394.1513085409.1513088642.5; __utmc=30149280; __utmz=30149280.1513085409.4.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.12366; __utma=223695111.1466963311.1510553394.1513085415.1513088642.4; __utmc=223695111; __utmz=223695111.1513085415.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=91F06ABA9A37C4CF5C5427FE13D29A1E|e49176fcf037708cda0f077adce2a508'}
url='https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=200&page_start=10'
response=requests.get(url,headers=header_dict).content
print response