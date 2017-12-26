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
name='逍遥法外'
url='http://xiazai003.com/osAuH2'
# header_dict = {'deviceType':'0','market':'appstore','appVersion':'4.7.6'}
response = requests.get(url).content
# print response
selector = html.fromstring(response)
# hrefs=selector.xpath('//*[@id="tab-g8-MP4"]/ul/li[1]/ul/li[5]/a')
downloadDic={}
path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
fo=open('%s/%s.txt'%(path,name),'w')

for x in xrange(1,8):

	# hrefs=selector.xpath('//*[@id="tab-g%s-720P"]/ul/li'%x)
	# if len(hrefs)==0:
		# hrefs=selector.xpath('//*[@id="tab-g%s-MP4"]/ul/li'%x)
	hrefs=selector.xpath('//*[@id="tab-g%s-MP4"]/ul/li'%x)
	# print len(hrefs) 
	seasonArr=[]
	seasonStr='%s第%s季'%(name,x)
	fo.write(seasonStr+':\n')
	for href in hrefs:
		numHref=href.xpath('ul/li/a/@href')
		# print len(numHref)
		# for x in numHref:
			# print x
		# xpathStr='ul/li[%s]/a/@href'%str(numberH-1) #城通
		xpathStr='ul/li[%s]/a/@href'%str(1) #迅雷
		# xpathStr='ul/li/a[contains(@href,"thunder")]/@href'

		# test=href.xpath('ul/li')
		# # test=href.xpath('ul/li/a[contains(@href,"thunder")]')
		# if test[0].xpath('a[contains(@href,"thunder")]'):
		# 	test2=test[0].xpath('a[contains(@href,"thunder")]/@href')
			# print test2

		# print test[0].xpath('@href')
		
		# print len(test)
		# xpathStr='ul/li/a[contains(@href,"magnet")]'
		# if href.xpath(xpathStr):
		# 	hre=href.xpath(xpathStr)

		# 	print hre[href]
		# else:
		# 	print 'kong'
		hre=href.xpath(xpathStr)
		seasonArr.append(hre[0])
		print hre[0]
		fo.write(hre[0]+'\n')
	
	downloadDic[seasonStr]=seasonArr
	# print len(seasonArr)
# print len(downloadDic)
# with open("downloadUrl.json","w") as f:
	# f.write(json.dumps(downloadDic,ensure_ascii=False))
# //*[@id="tab-g4-MP4"]/ul/li[1]/ul/li[1]/a
# //*[@id="tab-g5-HR-HDTV"]/ul/li[1]/ul/li[1]/a
# //*[@id="tab-g8-720P"]/ul/li[1]/ul/li[1]/a
# //*[@id="tab-g5-720P"]/ul/li[1]/ul/li[1]/a
# //*[@id="tab-g3-720P"]/ul/li[3]/ul/li[3]/a
