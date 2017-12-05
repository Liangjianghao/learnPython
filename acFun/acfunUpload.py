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



def login():
	option=webdriver.ChromeOptions()
	option.add_argument('--user-data-dir=/Users/l/Library/Application Support/Google/Chrome/Default')
	driver = webdriver.Chrome(chrome_options=option)
	# driver = webdriver.Chrome()

	driver.get("http://www.acfun.cn/login/")
	elemZH = driver.find_element_by_id("ipt-account-login")
	elemZH.send_keys('1084933098@qq.com')

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

	path='/Volumes/my/123'
	namelist=os.listdir(path)
	for fileM in namelist:
		if fileM=='.DS_Store':
			print ('存在DS_Store')
			os.remove(path+'/'+'.DS_Store')
			print ('删除DS_Store')
	for index,fileName in enumerate(namelist):

		filepath=path+'/'+fileName
		print ('进入循环'+str(index))
		if fileName=='.DS_Store':
			print ('存在DS_Store')
			continue

		driver.get('http://www.acfun.cn/member/#area=upload-video')
		time.sleep(3)
		name=cutStr(fileName)
		print (fileName)
		print (name)
		# titleInput = driver.find_element_by_id("title")
		# titleInput.send_keys(fileName)
		# time.sleep(3)

		# selectBtn=driver.find_element_by_name('channel')
		# # print len(contentList2)
		# Select(selectBtn).select_by_index(8)
		# time.sleep(3)

		# selectBtn2=driver.find_element_by_name('subject')
		# # print len(contentList2)
		# Select(selectBtn2).select_by_index(1)
		# time.sleep(3)


		# signBtn=driver.find_element_by_class_name('tagator_input')
		# print (name)
		# print ('gdg%s\n'%(fileName))
		# signBtn.send_keys('郭德纲\n%s\n'%(fileName))
		# time.sleep(3)
# input type=hidden

		# uploadFileBtn=driver.find_element_by_id('up-ready')
		# chain=ActionChains(driver)     
		# chain.move_to_element(uploadFileBtn).perform() 

# 		uploadFileBtn2=driver.find_element_by_id('upload-speed')

# 		value = driver.execute_script('return arguments[0].value;', uploadFileBtn2)
# 		print("Before update, hidden input value = {}".format(value))
# 		# ((JavascriptExecutor)driver).executeScript("arguments[0].checked = true;",uploadFileBtn2)
# 		driver.execute_script('''
#     var elem = arguments[0];
#     var value = arguments[1];
#     elem.value = value;
# ''', uploadFileBtn2, filepath)
# 		value = driver.execute_script('return arguments[0].value;', uploadFileBtn2)
# 		print("After update, hidden input value = {}".format(value))

		# print (len(uploadFileBtn2))
		# print (uploadFileBtn2)
		# uploadFileBtn2[0].send_keys(filepath)
		# time.sleep(60)

		# webuploader-element-invisible
		# uploadFileBtn=driver.find_element_by_class_name('webuploader-element-invisible')
		# uploadFileBtn.send_keys(filepath)

		uploadImgBtn=driver.find_element_by_id('up-pic')
		uploadImgBtn.click()

		print (uploadImgBtn.location)
		print (driver.switch_to.active_element.location)
		time.sleep(2)
		actions = ActionChains(driver);
		# actions.move_by_offset(20, -255).context_click().perform()
		actions.move_by_offset(20, -255).click().perform()
		print (driver.switch_to.active_element.location)
		driver.switch_to.active_element.send_keys('/Volumes/my/tu/565c4d584cc030e86893995a019f8ccb.png')

		time.sleep(15)

		# result=EC.alert_is_present()(driver)
		# if result:
		# 	print ('重新加载')
		# 	time.sleep(10)
		# 	result.accept()
		# else:
		# 	print ('未出现提示框')
		# time.sleep(2)



		# upload[22].send_keys(filepath)  # send_keys
		# time.sleep(120)

		# js="var q=document.documentElement.scrollTop=150"  
		# driver.execute_script(js) 

		# time.sleep(10)

		# FinishBtn=driver.find_element_by_id('submit_btn')
		# FinishBtn.click()
		# time.sleep(10)
		# os.remove(filepath)

		# driver.close()
		# driver.switch_to_window(driver.window_handles[0])

		# if index==7:
		# 	break
		time.sleep(10)
		driver.close()
driver=login()
fillPage(driver)