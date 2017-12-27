
# -- coding: UTF-8 -- 
import time
import sys
import os
from lxml import html
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
# reload(sys)
# sys.setdefaultencoding('utf8')
import random 
import re
from pygame import mixer 

def playMusic():
	
	mixer.init()
	mixer.music.load('1.mp3')
	mixer.music.play()
	time.sleep(1)
def nameGet():
    nameStr=''
    for x in range(1,5):
    	head = random.randint(0xb0, 0xf7)
    	body = random.randint(0xa1, 0xfe)
    	val = f'{head:x}{body:x}'
    	str = bytes.fromhex(val).decode('gb2312')
    	nameStr=nameStr+str
    return nameStr

driver=webdriver.Chrome()
driver.get("http://www.eobzz.com/afterPage/login.html")
time.sleep(3)

elemZH = driver.find_element_by_id("userName")
elemZH.send_keys('119074224')

elemMM = driver.find_element_by_id("userPass")
elemMM.send_keys("l31415926")
time.sleep(8)

print (driver.current_url)
fo = open("zhang.txt", "w")
for x in range(1,20):
	
	select = Select(driver.find_element_by_id("selP1")) 
	select.select_by_index(2)

	getMobileBtn=driver.find_element_by_id('getMobileBtn')
	getMobileBtn.click()
	time.sleep(3)
	phoneNum=driver.find_element_by_id('txtPhone')
	numberOfPhone = phoneNum.get_attribute("value")
	print (numberOfPhone)
	fo.write(numberOfPhone+'\n')
	js='window.open("http://www.acfun.cn/reg/");'
	driver.execute_script(js)
	time.sleep(3)
	driver.switch_to_window(driver.window_handles[1])
	print (driver.current_url)

	# print (driver.current_window_handle) # 输出当前窗口句柄（百度）
	# handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
	# print (handles)

	inputMobile=driver.find_element_by_id('ipt-mobile-reg').send_keys(numberOfPhone)
	inputUsername=driver.find_element_by_id('ipt-username-reg').send_keys(nameGet())
	inputpwd=driver.find_element_by_id('ipt-pwd-reg').send_keys('123456')
	inputRepwd=driver.find_element_by_id('ipt-repwd-reg').send_keys('123456')
	# .send_keys(Keys.ENTER)
	# inputRepwd=driver.find_element_by_id('ipt-repwd-reg').send_keys(Keys.ENTER)
	# time.sleep(5)
	# sendCode=driver.find_element_by_id('send-mobile-reg').click()
	playMusic()
	time.sleep(20)
	driver.switch_to_window(driver.window_handles[0])
	time.sleep(20)
	getCodeBtn=driver.find_element_by_id('btnCode').click()
	time.sleep(1)
	codeText=driver.find_element_by_id('codeContent')
	numberOfCode = codeText.get_attribute("value")
	if numberOfCode:
		print (numberOfCode)
	else:
		time.sleep(10)
		getCodeBtn=driver.find_element_by_id('btnCode').click()
		time.sleep(1)
		codeText=driver.find_element_by_id('codeContent')
		numberOfCode = codeText.get_attribute("value")

	code=re.findall(r"\d+\.?\d*",numberOfCode)[0]
	driver.switch_to_window(driver.window_handles[1])

	inputCode=driver.find_element_by_id('ipt-mobile-code').send_keys(code)
	inputCode=driver.find_element_by_id('ipt-mobile-code').send_keys(Keys.ENTER)
	time.sleep(5)
	driver.close() 
	driver.switch_to_window(driver.window_handles[0])

fo.close()







	