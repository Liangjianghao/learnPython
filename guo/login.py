# https://mp.weixin.qq.com/cgi-bin/loginpage?url=%2Fcgi-bin%2Fhome%3Ft%3Dhome%2Findex%26lang%3Dzh_CN%26token%3D1785036581
# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import math
from lxml import html
import urllib2

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# def updateImg：

def loadPage(zhanghao):
	driver = webdriver.Chrome()
	driver.get("https://www.douban.com/")

	# elemZH = driver.find_element_by_name("form_email")
	# elemZH.send_keys(zhanghao)

	# elemMM = driver.find_element_by_name("form_password")
	# elemMM.send_keys("l31415926")

	js="var q=document.documentElement.scrollTop=100"  
	driver.execute_script(js)  
	time.sleep(3) 

	return driver
def fillPage(driver):
	mineBtn = driver.find_element_by_class_name("bn-submit")
	mineBtn.click()
	# time.sleep(10)
	
	# cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	# cookiestr = ';'.join(item for item in cookie)  
	# print cookiestr

	# headers = {'cookie':cookiestr}  
	# homeurl="https://music.douban.com/"
	# req = urllib2.Request(homeurl, headers = headers)
	# responese=urllib2.urlopen(req)
	# text=responese.read()
	# print text
	# driver.manager().addCookie(cookiestr)
	# js="window.open('https://music.douban.com/')"
	# driver.execute_script(js)
	# time.sleep(2)
	# driver.get("https://music.douban.com/")
	time.sleep(2)
	# driver.get("https://music.douban.com/")
	# js = "var q=document.body.scrollTop=100000"  
	# driver.execute_script(js)  
	# time.sleep(3) 


	# js="var q=document.documentElement.scrollTop=100"  
	# driver.execute_script(js)  
	# time.sleep(3) 



driver=loadPage('1084933098@qq.com')
# fillPage(driver)

# driver.close()

# import re
# urlStr='https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=_(%22zh_CN%22)&token=1529046865'
# pattern = re.compile(r'token=(.*)')
# print re.findall(pattern,urlStr)


