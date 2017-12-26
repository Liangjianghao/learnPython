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
reload(sys)
sys.setdefaultencoding('utf8')


# def login():
# 	# driver = webdriver.PhantomJS()
# 	driver = webdriver.Chrome()
# 	driver.get("http://www.acfun.cn/login/")
# 	elemZH = driver.find_element_by_id("ipt-account-login")
# 	elemZH.send_keys('18621121232')

# 	elemMM = driver.find_element_by_id("ipt-pwd-login")
# 	elemMM.send_keys("l31415926")

# 	loginBtn = driver.find_element_by_class_name("btn-login")
# 	loginBtn.click()
# 	print driver.current_url
# 	time.sleep(10)
# 	print driver.page_source
# login()
def login():
	driver = webdriver.PhantomJS()
	# driver = webdriver.Chrome()
	driver.get("https://www.douban.com/")
	elemZH = driver.find_element_by_id("form_email")
	elemZH.send_keys('1084933098@qq.com')

	elemMM = driver.find_element_by_id("form_password")
	elemMM.send_keys("l31415926")

	loginBtn = driver.find_element_by_class_name("bn-submit")
	loginBtn.click()
	print driver.current_url
	time.sleep(30)
	# print driver.page_source
login()




# 480 报错
# https://movie.douban.com/subject/1291546/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia_video 详情
# driver=webdriver.Chrome()
# driver=webdriver.PhantomJS()
# driver.get('https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0')
# movieList=[]
# for x in xrange(1,2):
# 	# print x
# 	# if x==25:
# 		# break
# 	time.sleep(3)	
# 	# moreBtn=driver.find_element_by_class_name('more')
# 	# moreBtn.click()
# 	WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div[1]/div/div[4]/a"))).click()

# 	time.sleep(2)
# 	# cover-wp
# 	movieDetailItem=driver.find_elements_by_class_name('cover-wp')

# 	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]
# 	name='电影ID'  
# 	fo=open('%s/%s.txt'%(path,name),'w')

# 	print len(movieDetailItem)
	
# 	for index,x in enumerate(movieDetailItem):
# 		# print x.get_attribute('data-id')
# 		movieID=x.get_attribute('data-id')
# 		# print index
# 		movieList.append(movieID)
# 	print movieList








