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
reload(sys)
sys.setdefaultencoding('utf8')
def getSelector(url):	
	response=requests.get(url).content
	selector = html.fromstring(response)
	return selector
def getUrlByName(name):
	url='http://www.zimuzu.tv/search/index?keyword=%s&search_type='%name
	selector = getSelector(url)
	# hrefs=selector.xpath('//tr[contains(@class,"Scontent")]/td[@align]/@href')
	hrefs=selector.xpath('//div[@class="search-result"]/ul/li')
	name=hrefs[0].xpath('div[@class="clearfix search-item"]/em')
	print name[0].text
	newUrl=''
	if name[0].text=='电视剧':
		resource=hrefs[0].xpath('div[@class="clearfix search-item"]/div[@class="fl-img"]/a/@href')
		print resource[0]
		newUrl='http://www.zimuzu.tv%s'%resource[0]
	print len(hrefs)
	print newUrl
	driver=webdriver.PhantomJS()
	driver.get(newUrl)
	newSelector=html.fromstring(driver.page_source)
	downloadUrl=newSelector.xpath('//*[@id="resource-box"]/div/div/h3/a/@href')
	print downloadUrl[0]	
	return downloadUrl[0]
def writeToFile(name,url):
	response = requests.get(url).content
	selector = html.fromstring(response)
	downloadDic={}
	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
	fo=open('%s/%s.txt'%(path,name),'w')
	xunleiPath='%s/%s.txt'%(path,name)
	# //*[@id="menu"]
	menuHref=selector.xpath('//*[@id="menu"]/li')
	print len(menuHref)
	sessionNum=len(menuHref)-1
	# //*[@id="menu"]/li[6]/a
	zhoubian=selector.xpath('//*[@id="menu"]/li[%s]/a/text()'%len(menuHref))
	print zhoubian[0]
	if '季' in zhoubian[0]:
		sessionNum=sessionNum+1
	print name+'共搜索到资源'+str(sessionNum)+'季'
	# //*[@id="tab-g2-HR-HDTV"]/ul/li[1]/ul/li[1]/a

	for x in xrange(1,sessionNum+1):
		print x
		hrefs=selector.xpath('//*[@id="tab-g%s-MP4"]/ul/li'%x)
		if len(hrefs)==0:
			# hrefs=selector.xpath('//*[@id="tab-g%s-MP4"]/ul/li'%x)
			hrefs=selector.xpath('//*[@id="tab-g%s-720P"]/ul/li'%x)
		# hrefs=selector.xpath('//*[@id="tab-g%s-MP4"]/ul/li'%x)
		seasonArr=[]
		seasonStr='%s第%s季'%(name,x)
		fo.write(seasonStr+':\n')
		for href in hrefs:
			numHref=href.xpath('ul/li/a/@href')
			xpathStr='ul/li[%s]/a/@href'%str(1) #迅雷

			hre=href.xpath(xpathStr)
			seasonArr.append(hre[0])
			# print hre[0]
			fo.write(hre[0]+'\n')
	return xunleiPath

# getUrlByName('神盾局')
# name='神盾局'
def returnFile(name):
	return writeToFile(name,getUrlByName(name))


