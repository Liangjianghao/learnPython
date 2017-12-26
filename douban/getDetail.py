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
import pymysql
import datetime
import re
reload(sys)
sys.setdefaultencoding('utf8')

def insertChatContent(attrs,name,moviescore,category_name,movietime,uptime):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='127.0.0.1',
		port=3306,  
		user='root',  
		passwd='123456',  
		db='douban',  
		charset='utf8mb4'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO doubanMovieTable (createtime,attrs,name,moviescore,category_name,movietime,uptime) VALUES ( '%s','%s', '%s', '%s','%s','%s','%s')"  
	print sql
	data = (createtime,attrs,name,moviescore,category_name,movietime,uptime)  
	print uptime
	print name
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')

# timeT='1939-12-15(亚特兰大首映)'
# uptime=timeT.split('-')[0]
# insertChatContent('1','2','9.8','5','8',uptime)

driver=webdriver.Chrome()
data=[]
with open('dianying.json','r') as json_file:
    data = json.load(json_file)
for movie in data:
	url='https://movie.douban.com/subject/%s/?tag=豆瓣高分&from=gaia_video'%movie
	# url='https://movie.douban.com/subject/1291583/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia_video'
	print url
	driver.get(url)
	time.sleep(2)
	ele=driver.find_elements_by_class_name('pl')
	print len(ele)

	movieName=driver.find_element_by_xpath('//*[@id="content"]/h1/span[contains(@property,"v:itemreviewed")]')
	movieName=movieName.text.split(' ')[0]

	atrrs=driver.find_element_by_xpath('//*[@id="info"]/span[1]/span[2]/a')
	movieType=driver.find_elements_by_xpath('//*[@id="info"]/span[contains(@property,"v:genre")]')
	typeList=[]
	for type in movieType:
		typeList.append(type.text)		
	movieTypeStr=','.join(typeList)

	upTime=driver.find_element_by_xpath('//*[@id="info"]/span[contains(@property,"v:initialReleaseDate")]')
	upTime=upTime.text.split('-')[0]
	upTime = re.sub("\D", "", upTime)

	movieTime=driver.find_element_by_xpath('//*[@id="info"]/span[contains(@property,"v:runtime")]')
	movieScore=driver.find_element_by_xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong')
	insertChatContent(atrrs.text,movieName,movieScore.text,movieTypeStr,movieTime.text,upTime)


