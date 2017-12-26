# coding:utf-8

# CREATE TABLE `neihanRemenTable` (
#   `Id` int(11) NOT NULL AUTO_INCREMENT,
#   `create_time` datetime DEFAULT NULL COMMENT '创建时间',
#   `digg_count` varchar(255) DEFAULT NULL COMMENT '赞数',
#   `content` varchar(255) DEFAULT NULL COMMENT '内容',
#   `url` varchar(255) DEFAULT NULL COMMENT '网址',
#   `category_name` varchar(255) DEFAULT NULL COMMENT '类别',
#   `comments` varchar(255) DEFAULT NULL COMMENT '神评',
#   `time_param` int(11) DEFAULT NULL COMMENT '时间参数',
#   PRIMARY KEY (`Id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='内涵萌宠表';
import datetime
import time 
import requests
import json
import sys
import os
import pymysql
import time
def insertChatContent(create_time,digg_count,content,url,category_name,comments,maxtime):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='127.0.0.1',
		port=3306,  
		user='root',  
		passwd='123456',  
		db='neihanduanzi',  
		charset='utf8mb4'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO neihanRemenTable (create_time,digg_count,content,url,category_name,comments,time_param) VALUES ( '%s', '%s', '%s','%s','%s','%s','%s')"  
	savecontent = pymysql.escape_string(content)
	downUrl = pymysql.escape_string(url)
	category = pymysql.escape_string(category_name)
	comment = pymysql.escape_string(comments)
	time_param = pymysql.escape_string(maxtime)

	data = (createtime,digg_count,savecontent,downUrl,category,comments,time_param)  
	cursor.execute(sql % data)  
	connect.commit()  

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

def getContent(timeT):
	maxtime=timeT
	print (maxtime)
	mintime=time.time()-86400
	url='https://lf.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&city=安徽省&content_type=-101&count=30&double_col_mode=0&essence=1&latitude=31.07373374148812&longitude=121.4869591270161&message_cursor=175514038&min_time=%s&mpic=1&video_cdn_first=1'%int(maxtime)
	# url='http://lf.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=45&count=30&level=6&message_cursor=175514038&mpic=1&video_cdn_first=1'
	response=requests.get(url).content
	jsonData = json.loads(response)
	if jsonData['message']=='success':
		if jsonData['data']['max_time']:
			maxtime=jsonData['data']['max_time']

	while maxtime>mintime:
		try:
			print (maxtime)
			url='http://lf.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&content_type=-101&count=30&double_col_mode=0&essence=1&latitude=31.0738183616429&longitude=121.4869678883913&max_time=%s&message_cursor=175514038&mpic=1&video_cdn_first=1'%maxtime
			# url='https://lf.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=45&count=30&level=6&max_time=%s&message_cursor=175514038&mpic=1&video_cdn_first=1'%maxtime
			print (url)
			response=requests.get(url).content
			jsonData = json.loads(response)
			if jsonData['message']=='success':
				if jsonData['data']['max_time']:
					maxtime=jsonData['data']['max_time']
					print (maxtime)
					maxtime=timeDeal(str(maxtime))
					maxtime=float(maxtime)

					if len(jsonData['data']['tip'])>5:
						dataArr=jsonData['data']['data']
						for joker in dataArr:
							if 'group' in joker.keys():
								if 'download_url' in joker['group']:
									if joker['group']['digg_count']>10000:
										if joker['group']['text']:
											content=joker['group']['text'];
										else:
											content='略'
										if joker['group']['category_name']:
											category_name=joker['group']['category_name']
										else:
											category_name='未分类'
										if len(joker['comments'])>0:
											comments=joker['comments'][0]['text']
										else:
											comments='无神评'
										insertChatContent(joker['group']['create_time'],joker['group']['digg_count'],content,joker['group']['download_url'],category_name,comments,str(int(maxtime)))
				time.sleep(20)
		except Exception as e:
			raise

if __name__ == "__main__":

	getContent(time.time())