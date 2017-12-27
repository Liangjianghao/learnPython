
# -- coding: UTF-8 -- 
import time
import sys
import os
from lxml import html
import json
import requests
from selenium import webdriver

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import random  
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import re
def loginAcfun(driver,zhanghao,url):
	js='window.open("http://www.acfun.cn/login/");'
	driver.execute_script(js)
	time.sleep(3)
	driver.switch_to_window(driver.window_handles[1])

	elemZH = driver.find_element_by_id("ipt-account-login")
	elemZH.send_keys(zhanghao)

	elemMM = driver.find_element_by_id("ipt-pwd-login")
	elemMM.send_keys("123456")

	loginBtn = driver.find_element_by_class_name("btn-login")
	loginBtn.click()
	time.sleep(5)
	
	
	driver.get('http://www.acfun.cn/member/#area=splash')
	time.sleep(2)
	signBtn=driver.find_element_by_id('btn-sign-user').click()
	time.sleep(3)
	# //*[@id="block-user-left"]/div[1]/a
	# selector = html.fromstring(driver.page_source)
	# hrefs=selector.xpath('//table/tbody/tr')
	myName=driver.find_elements_by_class_name('name')
	# print len(myName)
	print '用户名:'+myName[1].text
	
	mybanana=driver.find_elements_by_class_name('pts')
	# print len(mybanana)
	print '香蕉数:'+mybanana[4].text

	myUID=driver.find_element_by_class_name('uid')
	print myUID.text
	time.sleep(3)

	if url:
		driver.get(url)
		time.sleep(3)

		js="var q=document.documentElement.scrollTop=500" 
		driver.execute_script(js) 

		toujiaoBtn=driver.find_elements_by_class_name('banana')
		# toujiaoBtn=driver.find_elements_by_id('bd_phoneshow')
		# bd_phoneshow
		print len(toujiaoBtn)
		chain=ActionChains(driver)     
		chain.move_to_element(toujiaoBtn[0]).perform()     #鼠标移到悬停元素上
		time.sleep(1)
		
		xiangjiaoBtn=driver.find_elements_by_class_name('bananaer')
		print len(xiangjiaoBtn)
		chain.move_to_element(xiangjiaoBtn[2]).click().perform()
		print 'yidianji'
		# time.sleep(3)
	else:
		print '只签到'
	driver.close()
	driver.switch_to_window(driver.window_handles[0])


# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)
# driver.get("http://www.acfun.cn/login/")

with open('zhanghao.txt', 'r') as f:  
    data = f.readlines() 
for zhanghao in data:
	print zhanghao.strip()
	loginAcfun(driver,zhanghao.strip(),'')
# loginAcfun(driver,'18474736838'.strip(),'')
	

