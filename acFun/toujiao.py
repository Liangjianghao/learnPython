
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
# reload(sys)
# sys.setdefaultencoding('utf8')
import re
def loginAcfun(zhanghao):
	driver = webdriver.Chrome()
	driver.get("http://www.acfun.cn/login/")
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
	time.sleep(300)
loginAcfun('13875765144')