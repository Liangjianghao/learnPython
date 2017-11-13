# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
import shutil
from lxml import html
import json
reload(sys)
sys.setdefaultencoding('utf8')
# print '123456'
# http://www.btans.com/search/%E9%95%BF%E5%9F%8E-first-asc-1
def analyUrl(name):
	url='http://www.btrabbit.cc/search/%s.html'%name
	print url	
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//div[@class="search-item detail-width"]')
	print len(hrefs)

	sourcelist=[]
	if len(hrefs)>0:
		href=hrefs[0]
		for x in hrefs:
			name=x.xpath('div[@class="item-title"]/h3/a/@title')
			nameStr=''
			# for x in name:
			nameStr=nameStr+name[0]
			detail=href.xpath('div[@class="item-bar"]/a/text()')
			# print detail[0]
			if detail:
				nameStr=nameStr+detail[0]
			sourcelist.append(nameStr)
			downUrl=x.xpath('div[@class="item-bar"]/a/@href')
			# print len(downUrl)
			sourcelist.append(downUrl[0])
			# for x in downUrl:
			# 	sourcelist.append(x)
			# # print len(sourcelist)
			if len(sourcelist)>4:
				break

	return sourcelist
def searchFH(name):
	seedstr = '\n'.join(analyUrl(name))
	# seedstr = analyUrl(name)
	# analyUrl(name)
	return	seedstr

KEY='70a315f07d324b3ea02cf21d13796605'
def answerQ(question):
    apiUrl='http://www.tuling123.com/openapi/api'
    # print apiUrl
    data={'key':KEY,'info':question,'userid':'qq'}
    # try:
    payload = {'key':KEY,'info':question}
    try:
		r=requests.post(apiUrl,data=payload)
		# print r.text
		mytext = json.loads(r.text)
		print mytext
		return mytext['text']
    except Exception as e:
    	# print e
		return '我也不知道,我再问问'
    # return result
 #    try:
 #    	r = requests.post(apiUrl, data=payload)
 #    	text = json.loads(r.text)
 #    	print text
	# except Exception as e:
 #    	print '超时'
print answerQ('上海天气')
# if __name__ == '__main__':
	# print '12333'
# print searchFH('生活大爆炸第一季')
