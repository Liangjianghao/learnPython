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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

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
def fillPage(driver):
	mineBtn = driver.find_elements_by_class_name("btn_login")
	mineBtn[0].click()
	time.sleep(10)
	
	url = driver.current_url
	# # print url
	pattern = re.compile(r'token=(.*)')
	tokenStr = re.findall(pattern,url)
	# print tokenStr
	cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	cookiestr = ';'.join(item for item in cookie)  
	# print cookiestr


	# headers = {'cookie':cookiestr}  
	# homeurl="https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=1709653932"
	# req = urllib2.Request(homeurl, headers = headers)
	# responese=urllib2.urlopen(req)
	# text=responese.read()
	# print text
	# driver.manager().addCookie(cookiestr)
	# driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=%s"%tokenStr[0])
	# driver.get("https://mp.weixin.qq.com/cgi-bin/filepage?type=2&begin=0&count=12&t=media/img_list&token=%s&lang=zh_CN"%tokenStr[0])
# https://mp.weixin.qq.com/cgi-bin/appmsg?begin=0&count=10&t=media/appmsg_list&type=10&action=list_card&lang=zh_CN&token=1814726619
	path='/Volumes/my/gdg'
	namelist=os.listdir(path)
	for index,fileName in enumerate(namelist):
		print (len(namelist))
		print (fileName)
		time.sleep(10)
		driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=%s"%tokenStr[0])
		time.sleep(10)
		filepath=path+'/'+fileName
		if fileName=='.DS_Store':
			continue
		# print filepath
		titleInput = driver.find_element_by_id("title")
		titleInput.send_keys(fileName)
		

		xiaoBtn=driver.find_elements_by_class_name('icon_radio')
		# print len(contentList2)
		xiaoBtn[3].click()

		upload=driver.find_elements_by_tag_name('input')
		# print len(upload)
		upload[22].send_keys(filepath)  # send_keys
		# print (upload[22].get_attribute('value'))  # check value
		time.sleep(120)

		# uploadBnt=driver.find_element_by_id('submit_btn')
		# uploadBnt.click()
		# time.sleep(10)
		js="var q=document.documentElement.scrollTop=100000"  
		driver.execute_script(js) 

		uploadBnt=driver.find_element_by_id('submit_btn')
		uploadBnt.click()
		os.remove(filepath)

		if index==8:
			break
		# print (driver.current_url)
		# continue



driver=loadPage('3523531761@qq.com')
fillPage(driver)
# fo.close()
# driver.close()

