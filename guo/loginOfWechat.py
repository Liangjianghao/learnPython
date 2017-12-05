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
	driver.get("https://mp.weixin.qq.com/cgi-bin/loginpage?url=%2Fcgi-bin%2Fhome%3Ft%3Dhome%2Findex%26lang%3Dzh_CN%26token%3D1785036581")

	elemZH = driver.find_element_by_name("account")
	elemZH.send_keys(zhanghao)

	elemMM = driver.find_element_by_name("password")
	elemMM.send_keys("l31415926")
	# cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	# cookiestr = ';'.join(item for item in cookie)  
	# print cookiestr
	# headers = {'cookie':cookiestr}  
	# homeurl="https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=1709653932"
	# req = urllib2.Request(homeurl, headers = headers)
	# print urllib2.urlopen(req)


	# driver.get("https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=1709653932")

	# https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=1709653932
	return driver
def fillPage(driver):

	# code=raw_input('waiting code\n')

	# elemCode = driver.find_element_by_id("randcode_input")
	# elemCode.clear()
	# elemCode.send_keys(code)
	# elemCode.send_keys(Keys.RETURN)
	# time.sleep(2)
	
	# result=EC.alert_is_present()(driver)
	# if result:
	# 	print'验证失败'
	# 	result.accept()

	# 	elemCode = driver.find_element_by_id("A_Loging_ChangeVerCode").click()

	# 	fillPage(driver)
	# else:

	mineBtn = driver.find_elements_by_class_name("btn_login")
	mineBtn[0].click()
	time.sleep(10)
	
	# cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
	# print cookie  
	# cookiestr = ';'.join(item for item in cookie)  
	# print cookiestr
	# headers = {'cookie':cookiestr}  
	# homeurl="https://mp.weixin.qq.com/cgi-bin/operate_voice?oper=voice_get&t=media/audio_add&lang=zh_CN&token=1709653932"
	# req = urllib2.Request(homeurl, headers = headers)
	# print urllib2.urlopen(req)


	contentList=driver.find_elements_by_link_text('素材管理')
	contentList[0].click()
	time.sleep(2)
	contentList2=driver.find_elements_by_link_text('图片')
	print len(contentList2)
	contentList2[0].click()

	# uploadBtn=driver.find_element_by_class_name('btn_primary')
	# uploadBtn.click()

	# print driver.page_source
	time.sleep(10)
	# Select(driver.find_element_by_name("table_files_length")).select_by_index(3)
	# titleInput=driver.find_element_by_class_name('title')
	# upload = driver.find_element_by_id('encodeid_hidden')
	# upload.send_keys('/Users/l/Desktop/learnPython/guo/gdg.txt')  # send_keys
	# print upload.get_attribute('value')  # check value

	# sreach_window=driver.current_window_handle 

	# titleInput.send_keys('测试')
	upload=driver.find_elements_by_tag_name('input')
	upload[0].send_keys('/Users/l/Desktop/learnPython/guo/image.png')  # send_keys
	# print upload[0].get_attribute('value')  # check value
	# print len(mainBtn)
	time.sleep(10)

	# # print driver.page_source
	# # fo.write(driver.page_source)
	# selector = html.fromstring(driver.page_source)
	# # hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
	# hrefs=selector.xpath('//table/tbody/tr')
	# # print len(hrefs)
	# for href in hrefs:
	# 	name=href.xpath('td/div/a')
	# 	# print name[0].text
	# 	url=href.xpath('td/div/a/@href')
	# 	# print url[0]
	# 	fo.write(name[0].text+'\n'+url[0]+'\n')
	# nextPage=driver.find_elements_by_class_name('paginate_button')
	# pageNum=int(nextPage[len(nextPage)-2].text)
	# # print pageNum
	# for x in xrange(1,pageNum):
	# 	nextPage=driver.find_elements_by_class_name('paginate_button')
	# 	nextPage2=nextPage[len(nextPage)-1].find_element_by_tag_name('a')
	# 	nextPage2.click()
	# 	time.sleep(3)
	# 	selector = html.fromstring(driver.page_source)
	# 	# hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
	# 	hrefs=selector.xpath('//table/tbody/tr')
	# 	# print len(hrefs)
	# 	for href in hrefs:
	# 		name=href.xpath('td/div/a')
	# 		# print name[0].text
	# 		url=href.xpath('td/div/a/@href')
	# 		# print url[0]
	# 		fo.write(name[0].text+'\n'+url[0]+'\n')

# path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
# fo=open('%s/gdgcnn.txt'%(path),'w')

driver=loadPage('3523531761@qq.com')
fillPage(driver)
# fo.close()
# driver.close()

