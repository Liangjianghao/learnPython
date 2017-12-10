# https://mp.weixin.qq.com/cgi-bin/loginpage?url=%2Fcgi-bin%2Fhome%3Ft%3Dhome%2Findex%26lang%3Dzh_CN%26token%3D1785036581
# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import math
from lxml import html
# import urllib2
import re
import json

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
import sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf8')



def login():
	option=webdriver.ChromeOptions()
	option.add_argument('--user-data-dir=/Users/l/Library/Application Support/Google/Chrome/Default')
	# driver = webdriver.Chrome(chrome_options=option)
	driver = webdriver.Chrome()

	driver.get("http://www.acfun.cn/login/")
	elemZH = driver.find_element_by_id("ipt-account-login")
	elemZH.send_keys('18621121232')

	elemMM = driver.find_element_by_id("ipt-pwd-login")
	elemMM.send_keys("l31415926")

	# time.sleep(3)
	loginBtn = driver.find_element_by_class_name("btn-login")
	loginBtn.click()
	time.sleep(5)

	return driver
def cutStr(name):
	resultStr=''
	if ' ' in name :
		for index,NameStr in enumerate(name.split(' ')):
			if index==0:
				continue
			else:
				resultStr+=NameStr
	else:
		resultStr=name
	resultStr=resultStr.split('.')[0]
	resultStr=resultStr.replace('（','').replace('）','').replace('《','').replace('》',' ')
	resultStr=re.sub(r"[\t,^\d{n}]",'',resultStr)

	return resultStr
def idChange(strID):
	newID=strID.split('/')[2]
	print newID
	newID=newID.replace('ac','')
	print newID
	return newID

def fillPage(driver):
	url = driver.current_url
	# print url
	pattern = re.compile(r'token=(.*)')
	tokenStr = re.findall(pattern,url)
	# print tokenStr
	cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	cookiestr = ';'.join(item for item in cookie)  

	# http://www.acfun.cn/member/#area=upload-video

	# for index,fileName in enumerate(namelist):

	# print ('进入循环'+str(index))

	driver.get('http://www.acfun.cn/member/#area=post-history')
	time.sleep(3)
	pageNum=driver.find_element_by_class_name('ipt-pager').get_attribute('data-max')
	pageNum=int(pageNum)
	proList=[]
	for x in xrange(1,pageNum):
		selector = html.fromstring(driver.page_source)
		# hrefs=selector.xpath('//div[@id="list-manage-manage"]/div/*/p[@class="block-title"]')
		hrefs=selector.xpath('//p[@class="block-title"]/a')
		# print len(hrefs)

		for href in hrefs:
			proDic={}
			name=href.xpath('text()')
			acID=href.xpath('@href')
			acID=idChange(acID[0])
			# print name[0]
			# print acID[0]
			proDic[name[0]]=acID
			proList.append(proDic)
		    # print(href.xpath('text()'))
		    # print(href.xpath('@href'))
		    # print href.text
		# btn-pager
		# print str(x+1)
		pageBtn=driver.find_element_by_class_name('ipt-pager').send_keys(str(x+1))
		swithBtn=driver.find_element_by_class_name('btn-pager').click()
		time.sleep(2)
	# print proList
	json_str = json.dumps(proList,ensure_ascii=False)
	print json_str
	with open("1.json","w") as f:
		f.write(json.dumps(proList,ensure_ascii=False))
		print("加载入文件完成...")
	for pro in proList:
		# print pro
		for k in pro:
		    print "%s=" % k,pro[k]

		# print pro.keys[0]
		# print pro.values[0]

driver=login()
fillPage(driver)