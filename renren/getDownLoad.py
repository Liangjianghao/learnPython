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
url='http://xiazai003.com/lvtzq3'
# header_dict = {'deviceType':'0','market':'appstore','appVersion':'4.7.6'}
response = requests.get(url).content
# print response
selector = html.fromstring(response)
# hrefs=selector.xpath('//*[@id="tab-g8-MP4"]/ul/li[1]/ul/li[5]/a')

hrefs=selector.xpath('//*[@id="tab-g8-MP4"]/ul/li')
print len(hrefs)

for href in hrefs:
	numHref=href.xpath('ul/li')
	numberH=len(numHref)
	# print numberH
	xpathStr='ul/li[%s]/a/@href'%str(numberH-1)
	hre=href.xpath(xpathStr)
	print hre
	# url='https://zimuzuustv.ctfile.com/fs/1939455-228422415'
	url=hre[0]
	driver=webdriver.Chrome()
	driver.get(url)
	time.sleep(5)
	downLoadBtn=driver.find_element_by_id("free_down_link")
	downLoadBtn.click()
	time.sleep(5)
	print driver.current_url
	downLoadBtn2=driver.find_element_by_id("free_down_link")
	downLoadBtn2.click()
	time.sleep(20)
	# driver.close()
time.sleep(3600)
# //*[@id="tab-g8-MP4"]/ul/li[2]/ul/li[5]/a
# //*[@id="tab-g4-MP4"]/ul/li[3]/ul/li[5]/a


