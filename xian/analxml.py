# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
from lxml import html
import  xml.dom.minidom
from lxml import etree


reload(sys)
sys.setdefaultencoding('utf8')
# http://www.btans.com/search/%E9%95%BF%E5%9F%8E-first-asc-1
# dom = xml.dom.minidom.parse('1.xml')
xml_file = etree.parse(r'1.xml')
# root_node = xml_file.getroot()
hrefs=xml_file.xpath('//d')
listTime=[]
for href in hrefs:
	# print href.text 
	if '哈哈' in href.text:
		time=href.xpath('@p')
		# print time[0]
		timeStr=str(time[0])
		# killStr=','
		if '.' in timeStr:
			flist=timeStr.split('.')
			# print flist[0]
			# print len(flist[0])
			listTime.append(flist[0])

# print listTime
numbers = map(int, listTime)
numbers.sort()
print numbers

for number in numbers:
	m, s = divmod(number, 60)
	h, m = divmod(m, 60)
	print ("%02d:%02d:%02d" % (h, m, s))


# selector = html.fromstring(xml_file)

# print selector

# def analyUrl(name):
# 	# url='http://www.btans.com/search/%s-first-asc-1'%name
# 	# print url	
# 	# response=requests.get(url).content
# 	dom = xml.dom.minidom.parse('abc.xml')

# 	selector = html.fromstring(response)
# 	hrefs=selector.xpath('//div[@class="search-item"]')
# 	sourcelist=[]
# 	if len(hrefs)>0:
# 		href=hrefs[0]
# 		name=href.xpath('div[@class="item-title"]/a/span')
# 		sourcelist.append(name[0].text)
# 		downUrl=href.xpath('div[@class="item-bar"]/a/@href')
# 		# print len(downUrl)
# 		for x in downUrl:
# 			sourcelist.append(x)
# 	return sourcelist
# def searchFH(name):
# 	seedstr = '\n'.join(analyUrl(name))
# 	return	seedstr
# print searchFH('长城')
