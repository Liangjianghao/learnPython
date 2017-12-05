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
	# driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=%s"%tokenStr[0])
	path='/Volumes/my/gdg'
	namelist=os.listdir(path)
	for fileM in namelist:
		if fileM=='.DS_Store':
			print ('存在DS_Store')
			os.remove(path+'/'+'.DS_Store')
			print ('删除DS_Store')
	for index,fileName in enumerate(namelist):
		# driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=%s"%tokenStr[0])
		filepath=path+'/'+fileName
		print ('进入循环'+str(index))
		if fileName=='.DS_Store':
			print ('存在DS_Store')
			continue
		# print (len(namelist))
		# driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=%s"%tokenStr[0])
		# driver.refresh()
		# driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=%s"%tokenStr[0])
		driver.get('https://mp.weixin.qq.com/cgi-bin/filepage?type=3&begin=0&count=21&t=media/list&token=%s&lang=zh_CN'%tokenStr[0])
		resultA=EC.alert_is_present()(driver)
		if resultA:
			print ('重新加载1')
			# time.sleep(2)
			result.accept()
		else:
			print ('未出现提示框')
		uploadBtn=driver.find_element_by_class_name('btn_primary')
		uploadBtn.click()
		driver.switch_to_window(driver.window_handles[1])
		time.sleep(2)
		print (driver.title)

		result=EC.alert_is_present()(driver)
		if result:
			print ('重新加载2')
			# time.sleep(2)
			result.accept()
		else:
			print ('未出现提示框')
		time.sleep(2)
		print (driver.current_url)
		name=cutStr(fileName)
		print ('fileName'+fileName)
		print ('name-'+name)
		titleInput = driver.find_element_by_id("title")
		titleInput.send_keys(name)
		time.sleep(3)

		xiaoBtn=driver.find_elements_by_class_name('icon_radio')
		# print len(contentList2)
		xiaoBtn[3].click()
		time.sleep(3)

		upload=driver.find_elements_by_tag_name('input')
		print (len(upload))

		# JavascriptExecutor jse=(JavascriptExecutor)driver
		# jse.executeScript('scroll(0,250)')

		upload[22].send_keys(filepath)  # send_keys
		time.sleep(120)
		# time.sleep(2)
		# WebDriverWait wait = new WebDriverWait(driver, 15);
		# wait.until(ExpectedConditions.elementToBeClickable(By.id("submit_btn")));
		# WebDriverWait wait = new WebDriverWait(driver,15)

		js="var q=document.documentElement.scrollTop=150"  
		driver.execute_script(js) 

		time.sleep(10)

		FinishBtn=driver.find_element_by_id('submit_btn')
		FinishBtn.click()
		time.sleep(10)
		os.remove(filepath)

		driver.close()
		driver.switch_to_window(driver.window_handles[0])

		if index==7:
			break

		# WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.ID,'submit_btn')).click()

		# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='submit_btn']"))).click()
		# element = driver.findElement(By("//*[@id='submit_btn"));

		# actions = ActionChains(driver);

		# actions.moveToElement(element).click().perform();

driver=loadPage('3523531761@qq.com')
fillPage(driver)