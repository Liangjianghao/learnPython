# -- coding: UTF-8 -- 
import sys
import os
import os.path
import urllib
import sys
import json
import requests
from lxml import html
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

reload(sys)
sys.setdefaultencoding('utf8')

# 480 报错
# https://movie.douban.com/subject/1291546/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia_video 详情
driver=webdriver.Chrome()
driver.get('https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0')
movieList=[]
for x in xrange(1,25):
	print x
	if x==25:
		break
	time.sleep(3)	
	# moreBtn=driver.find_element_by_class_name('more')
	# moreBtn.click()
	WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div[1]/div/div[4]/a"))).click()

	time.sleep(2)
	# cover-wp
	movieDetailItem=driver.find_elements_by_class_name('cover-wp')

	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]
	name='电影ID'  
	fo=open('%s/%s.txt'%(path,name),'w')

	print len(movieDetailItem)
	
	for index,x in enumerate(movieDetailItem):
		# print x.get_attribute('data-id')
		movieID=x.get_attribute('data-id')
		# print index
		movieList.append(movieID)

with open("dianying.json","w") as f:
	f.write(json.dumps(movieList,ensure_ascii=False))






