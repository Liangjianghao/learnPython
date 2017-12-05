# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
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

		elemCode = driver.find_element_by_id("A_Loging_ChangeVerCode").click()

		fillPage(driver)
	else:

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
			fo.write(name[0].text+'\n'+url[0]+'\n')
		nextPage=driver.find_elements_by_class_name('paginate_button')
		pageNum=int(nextPage[len(nextPage)-2].text)
		# print pageNum
		for x in xrange(1,pageNum):
			nextPage=driver.find_elements_by_class_name('paginate_button')
			nextPage2=nextPage[len(nextPage)-1].find_element_by_tag_name('a')
			nextPage2.click()
			time.sleep(3)
			selector = html.fromstring(driver.page_source)
			# hrefs=selector.xpath('//div[@id="table_files_wrapper"]')
			hrefs=selector.xpath('//table/tbody/tr')
			# print len(hrefs)
			for href in hrefs:
				name=href.xpath('td/div/a')
				# print name[0].text
				url=href.xpath('td/div/a/@href')
				# print url[0]
				fo.write(name[0].text+'\n'+url[0]+'\n')

path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
fo=open('%s/gdgcnn.txt'%(path),'w')

driver=loadPage('1084933098@qq.com')
fillPage(driver)
fo.close()
# driver.close()

