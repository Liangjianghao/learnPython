import datetime
import time 
import requests
import json
import sys
import os
import pymysql
# import tool
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def timeDeal(maxtime):
	if '.' not in maxtime:
		return maxtime

	rightT=maxtime.split('.')[1]
	leftT=maxtime.split('.')[0]
	if len(rightT)==1:
		return leftT
	if len(rightT)>6:
		t=rightT[-1]
		s=rightT[-3:-1]
		r=rightT[:4]
		# if t is '9' or t is '8' :
		if int(t)>5 :
			print ('+1')
			s=int(s)+1
			s=str(s)[-2] if s%10==0 else str(s)
			rightT=r+s
		else:
			print ('right')
		print (leftT+'.'+rightT)
		return leftT+'.'+rightT
	else:
		return maxtime
	
global maxtime
def firstRequest():
	url='http://iu.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=3&count=30&level=6&message_cursor=175514038&mpic=1&video_cdn_first=1'
	response=requests.get(url).content
	jsonData = json.loads(response)
	if jsonData['message']=='success':
		maxtime=jsonData['data']['max_time']
		# print (maxtime)

global i
# print (json.dumps(dic))
# maxtime='1513405847'

firstRequest()
# maxtime=str(time.time()).split('.')[0]
# print (maxtime)
# maxtime=int(maxtime)
# mintime=maxtime-86400
# print (maxtime)
global maxtime
url='http://iu.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=3&count=30&level=6&message_cursor=175514038&mpic=1&video_cdn_first=1'
response=requests.get(url).content
jsonData = json.loads(response)
if jsonData['message']=='success':
	maxtime=jsonData['data']['max_time']
# maxtime='1513401418'
i=1
# while maxtime>mintime:
while 1:
	url='http://iu.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=3&count=30&level=6&max_time=%s&message_cursor=175514038&mpic=1&video_cdn_first=1'%maxtime
	# print (url)
	response=requests.get(url).content
	jsonData = json.loads(response)

	if jsonData['message']=='success':
		i+=1
		maxtime=jsonData['data']['max_time']
		# print (jsonData['data'])
		print (maxtime)
		maxtime=timeDeal(str(maxtime))
		print (maxtime)
		maxtime=float(maxtime)
		time.sleep(20)
		if i>30:
			break
