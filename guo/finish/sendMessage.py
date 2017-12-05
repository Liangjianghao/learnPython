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
from selenium.webdriver.common.action_chains import *

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
	for index,NameStr in enumerate(name.split(' ')):
		if index==0 or index==1:
			continue
		else:
			resultStr+=NameStr
	# print resultStr
	resultStr=resultStr.split('.')[0]
	return resultStr

def fillPage(driver):
	mineBtn = driver.find_elements_by_class_name("btn_login")
	mineBtn[0].click()
	time.sleep(10)
	
	url = driver.current_url
	# print url
	pattern = re.compile(r'token=(.*)')
	tokenStr = re.findall(pattern,url)
	# if tokenStr:
	# 	continue
	print (tokenStr)
	cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	cookiestr = ';'.join(item for item in cookie)  
	# print cookiestr

	driver.get("https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&lang=zh_CN&token=%s"%tokenStr[0])
	# audio_music_plugin_btn
	time.sleep(5)
	for x in range(1,9):
		# print (driver.switch_to.active_element.location)
		# if x==1:
		# 	print ('音频')
		# else:
		# 	print ('其他')
		# 	actions = ActionChains(driver);
		# 	actions.move_by_offset(260, 400).click().perform()
		# 	time.sleep(3)
		# driver.switch_to.active_element.send_keys('音频 \n')
		# time.sleep(10)
	# 选择音频页面
		mp3Btn=driver.find_element_by_id('audio_music_plugin_btn')
		mp3Btn.click()
		time.sleep(2)
	#选择音频	
		xiaoBtn=driver.find_elements_by_class_name('audio_title')
		xiaoBtn[x-1].click()
		time.sleep(2)
		name=xiaoBtn[x-1].text

	# 音频确定
		confirmBtn=driver.find_element_by_class_name('js_btn')
		confirmBtn.click()

		# print (driver.switch_to.active_element.location)
		driver.switch_to.active_element.send_keys(name)
		time.sleep(10)
	# 标题
		titleInput = driver.find_element_by_id("title")
		titleInput.send_keys(name)
		time.sleep(3)
		# author
	# 作者
		authorInput = driver.find_element_by_id("author")
		authorInput.send_keys('大铁棍子')
		time.sleep(3)
	#图片选择
		js="var q=document.documentElement.scrollTop=1000"  
		driver.execute_script(js)  
		time.sleep(3) 
		imgSelectBtn=driver.find_element_by_id('js_imagedialog')
		imgSelectBtn.click()
		time.sleep(3)
	# 图片列表
		imglist=driver.find_element_by_class_name('img_list')
		# print (imglist)

		imgSelect=driver.find_elements_by_class_name('js_imageitem')
		# print (len(imgSelect))
		imgSelect[x-1].click()

		imgConfirmBtn=driver.find_elements_by_class_name('js_btn')
		# print (len(imgConfirmBtn))
		imgConfirmBtn[0].click()
		time.sleep(3)

		imgConfirmBtn[2].click()
		time.sleep(3)


		js="var q=document.documentElement.scrollTop=100000" 
		# js="var q=document.documentElement.scrollTop=50"  

		driver.execute_script(js) 

		showNextBtn=driver.find_element_by_class_name('add_gray')
		# print (showNextBtn.text)

		chain=ActionChains(driver)     
		chain.move_to_element(showNextBtn).perform()
		time.sleep(1)     #鼠标移到悬停元素上
		if x>=4:
			# js="document.getElementByClassName('scroll-bar')[0].scrollDown=100"  
			js="var q=document.getElementsByClassName('scroll-bar')[0].scrollTop=100000" 
			driver.execute_script(js) 
			time.sleep(5) 
		if x==8:
			break
		nextBtn=driver.find_element_by_class_name('icon_appmsg_create')
		nextBtn.click()
		time.sleep(2)


# 确定群发
	allConfirmBtn=driver.find_elements_by_id('js_send')
	print (len(allConfirmBtn))
	allConfirmBtn[0].click()


driver=loadPage('3523531761@qq.com')
fillPage(driver)