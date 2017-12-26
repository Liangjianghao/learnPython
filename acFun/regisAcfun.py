
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
def openSuma(driver):
	driver = webdriver.Chrome()
	driver.get("http://www.acfun.cn/reg/")
	elemZH = driver.find_element_by_id("ipt-account-login")
	elemZH.send_keys('1084933098@qq.com')

	elemMM = driver.find_element_by_id("ipt-pwd-login")
	elemMM.send_keys("l31415926")

	loginBtn = driver.find_element_by_class_name("btn-login")
	loginBtn.click()
	time.sleep(3)

# userName = ''.join(random.sample("1234567890abcdefghijklmnopqrstuvw",8)) 

# def nameGet():
#     nameStr=''
#     for x in range(1,5):
#     	head = random.randint(0xb0, 0xf7)
#     	body = random.randint(0xa1, 0xfe)
#     	val = f'{head:x}{body:x}'
#     	str = bytes.fromhex(val).decode('gb2312')
#     	nameStr=nameStr+str
#     return nameStr
# print (nameGet())

strName='【AcFun弹幕视频网】您的验证码为：271858。一起加入弹幕的世界，AC娘等你来玩哦(＾o＾)丿验证码5分钟内有效。'

print re.findall(r"\d+\.?\d*",strName)[0]

