# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import chargeAlert
import math
from lxml import html

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
import getstring
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# def updateImg：

def loadPage(zhanghao):
	driver = webdriver.Chrome()
	driver.get("https://www.ctfile.com/index.php?item=account&action=login&ref=https%3A//www.ctfile.com/")

	elemZH = driver.find_element_by_id("inputEmail")
	elemZH.send_keys(zhanghao)

	elemMM = driver.find_element_by_id("inputPassword")
	elemMM.send_keys("l31415926")
	# elemte = driver.find_element_by_class_name("control-label")
	# print elemte.text
	# time.sleep(3)
	return driver
def fillPage(driver):

	code=raw_input('waiting code\n')

	elemCode = driver.find_element_by_id("randcode_input")
	elemCode.clear()
	elemCode.send_keys(code)
	elemCode.send_keys(Keys.RETURN)
	time.sleep(2)
	
	result=EC.alert_is_present()(driver)
	if result:
		print'验证失败'
		result.accept()
		# driver.close()
		# time.sleep(3)
		elemCode = driver.find_element_by_id("A_Loging_ChangeVerCode").click()

		fillPage(driver)
	else:
		# print '验证成功'
		# time.sleep(3)
		# print 'nothing'

		# loginBtn = driver.find_element_by_class("btn btn-primary btn-large").click()
		mineBtn = driver.find_elements_by_class_name("_tooltip")
		mineBtn[0].click()
		time.sleep(2)
		

		contentList=driver.find_elements_by_link_text('相声大全')
		contentList[0].click()
		time.sleep(2)
		contentList2=driver.find_elements_by_link_text('丑娘娘')
		# print len(contentList2)
		contentList2[0].click()
		

		# print driver.page_source
		time.sleep(3)
		Select(driver.find_element_by_name("table_files_length")).select_by_index(3)
		time.sleep(5)

		# print driver.page_source
		# fo.write(driver.page_source)
		selector = html.fromstring(driver.page_source)
		# hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
		hrefs=selector.xpath('//table/tbody/tr')
		# print len(hrefs)
		for href in hrefs:
			name=href.xpath('td/div/a')
			# print name[0].text
			url=href.xpath('td/div/a/@href')
			# print url[0]
			fo.write(name[0].text+' '+url[0]+'\n')

		
			# print len(nextPage)
		# nextPage2=nextPage[len(nextPage)-1].find_element_by_tag_name('a')
		# for x in nextPage:
		# 	print x.text
		# 	print x.get_attribute('class')
		# 	print x.get_attribute('name')
		# print nextPage[len(nextPage)-2].text


		
		# pageNum=int(nextPage[len(nextPage)-2].text)-1
		# print pageNum
		# for x in xrange(1,pageNum):
		# 	# print 'page'+str(x）
		# 	nextPage=driver.find_elements_by_class_name('paginate_button')
		# 	nextPage2=nextPage[len(nextPage)-1].find_element_by_tag_name('a')
		# 	nextPage2.click()
		# 	time.sleep(3)
		# 	selector = html.fromstring(driver.page_source)
		# 	# hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
		# 	hrefs=selector.xpath('//table/tbody/tr')
		# 	print len(hrefs)
		# 	for href in hrefs:
		# 		name=href.xpath('td/div/a')
		# 		# print name[0].text
		# 		url=href.xpath('td/div/a/@href')
		# 		# print url[0]
		# 		fo.write(name[0].text+' '+url[0]+'\n')
		# 	time.sleep(3)



		# while 1:
		# 	if not nextPage2.text:
				
		# 		print 'continue'
		# 		nextPage2.click()
		# 		time.sleep(3)
		# 		continue
		# 	elif nextPage2!=100:
		# 		print'!=100'
		# 		nextPage2.click()
		# 		time.sleep(3)
		# 		continue

		# 	print 'enter while'
			

		# 	# nextPage=driver.find_elements_by_tag_name('a')
		# 	# for page in nextPage:
		# 	# 	print page.text
		# 		# if  eval('3').equals(page.text):
		# 		# 	print'fanye'
		# 		# 	page.click()
		# 	time.sleep(3)
		# 	selector = html.fromstring(driver.page_source)
		# 	# hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
		# 	hrefs=selector.xpath('//table/tbody/tr')
		# 	print len(hrefs)
		# 	for href in hrefs:
		# 		name=href.xpath('td/div/a')
		# 		# print name[0].text
		# 		url=href.xpath('td/div/a/@href')
		# 		# print url[0]
		# 		fo.write(name[0].text+' '+url[0]+'\n')



		# contentList3=driver.find_elements_by_link_text('说学逗唱 岳云鹏 于谦.mp3')
		# print len(contentList3)
		# # contentList3[0].click()
		# print contentList3[0].get_attribute('href')

		# print len(contentList)
		# mineBtn = driver.find_elements_by_class_name("_tooltip").click()
		# print len(mineBtn)

		# links = driver.find_elements_by_tag_name("a")  
		# for link in links:
		# 	print link.get_attribute('class')

		# jifen = driver.find_element_by_id("TD_Run_Score")
		# guajishu=driver.find_element_by_id("Span_Run_OnNum")
		# guajishuT=driver.find_element_by_id("Span_Run_MaxNum")
		# print zhanghao+'--积分：'+jifen.text+'--在线:'+guajishu.text+'\n'
		# fo.write(zhanghao+'--积分：'+jifen.text+'--在线:'+guajishu.text+'\n')
		# driver.close()



path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
fo=open('%s/gdg2.txt'%(path),'w')

driver=loadPage('1084933098@qq.com')
fillPage(driver)
fo.close()
# driver.close()

