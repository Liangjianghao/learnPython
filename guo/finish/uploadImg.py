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
# reload(sys)
# sys.setdefaultencoding('utf8')

# def updateImg：

def loadPage(zhanghao):
	driver = webdriver.Chrome()
	# driver.get("https://mp.weixin.qq.com/cgi-bin/loginpage?url=%2Fcgi-bin%2Fhome%3Ft%3Dhome%2Findex%26lang%3Dzh_CN%26token%3D1785036581")
	driver.get("https://mp.weixin.qq.com/")

	elemZH = driver.find_element_by_name("account")
	elemZH.send_keys(zhanghao)

	elemMM = driver.find_element_by_name("password")
	elemMM.send_keys("l31415926")

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

def fillPage(driver):
	mineBtn = driver.find_elements_by_class_name("btn_login")
	mineBtn[0].click()
	time.sleep(20)
	
	url = driver.current_url
	# print url
	pattern = re.compile(r'token=(.*)')
	tokenStr = re.findall(pattern,url)
	# print tokenStr
	cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	cookiestr = ';'.join(item for item in cookie)  

	path='/Volumes/my/tu'
	namelist=os.listdir(path)
	driver.get('https://mp.weixin.qq.com/cgi-bin/filepage?type=2&begin=0&count=12&t=media/img_list&token=%s&lang=zh_CN'%tokenStr[0])

	for fileM in namelist:
		if fileM=='.DS_Store':
			os.remove(path+'/'+'.DS_Store')
	for index,fileName in enumerate(namelist):
		filepath=path+'/'+fileName
		print ('进入循环'+str(index))
		if fileName=='.DS_Store':
			print ('存在DS_Store')
			continue		
		time.sleep(2)
	# uploadImgBtn=driver.find_element_by_id('')
		upload=driver.find_elements_by_tag_name('input')
		print (len(upload))
		upload[0].send_keys(filepath)		
		time.sleep(5)
		if index==7:
			break

driver=loadPage('3523531761@qq.com')
fillPage(driver)