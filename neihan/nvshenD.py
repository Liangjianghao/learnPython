# coding:utf-8

# CREATE TABLE `nvshenTable` (
#   `Id` int(11) NOT NULL AUTO_INCREMENT,
#   `create_time` datetime DEFAULT NULL COMMENT '创建时间',
#   `digg_count` varchar(255) DEFAULT NULL COMMENT '赞数',
#   `content` varchar(255) DEFAULT NULL COMMENT '内容',
#   `url` varchar(255) DEFAULT NULL COMMENT '网址',
#   `category_name` varchar(255) DEFAULT NULL COMMENT '类别',
#   `comments` varchar(255) DEFAULT NULL COMMENT '神评',
#   PRIMARY KEY (`Id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='内涵女神表';
import datetime
import time 
import requests
import json
import sys
import os
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def insertChatContent(create_time,digg_count,content,url,category_name,comments):
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
	sql = "INSERT INTO nvshenTable (create_time,digg_count,content,url,category_name,comments) VALUES ( '%s', '%s', '%s','%s','%s','%s')"  
	print sql
	# create_time = pymysql.escape_string(create_time)
	# print create_time
	# content_type = pymysql.escape_string(content_type)
	savecontent = pymysql.escape_string(content)
	downUrl = pymysql.escape_string(url)
	category = pymysql.escape_string(category_name)
	comment = pymysql.escape_string(comments)

	data = (createtime,digg_count,savecontent,downUrl,category,comment)  
	# print data
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')
def getContent():
	maxtime=1510035012
	while True:
		try:
			maxtime=maxtime-2
			# url='http://is.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&content_type=-101&count=30&double_col_mode=0&essence=1&latitude=31.07387527647243&longitude=121.4869829908048&max_time=%s&message_cursor=175514038&mpic=1&video_cdn_first=1'%maxtime
			url='http://is.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=12&count=30&level=6&max_time=%s&message_cursor=175514038&mpic=1&video_cdn_first=1'%maxtime
			# url=getUrl()
			# print url
			response=requests.get(url).content
			# print response
			jsonData = json.loads(response)
			# print jsonData
			if jsonData['message']=='success':
				if len(jsonData['data']['tip'])>5:
					dataArr=jsonData['data']['data']
					# print len(dataArr)
					for joker in dataArr:
						# if joker.has_key('group'):
						if 'group' in joker.keys():
							# print joker['group']['digg_count']
							print joker['group']['text']
							# print joker['group']['create_time']
							if 'download_url' in joker['group']:
								# print joker['group']['mp4_url']
							# share_url 漫画
								print joker['group']['digg_count']
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

									print category_name+ comments
									insertChatContent(joker['group']['create_time'],joker['group']['digg_count'],content,joker['group']['download_url'],category_name,comments)
							# bury_count 踩 comment_count 评论 share_count 转发 comments array。count》0 神评 category_name 类型 
							# share_url for 101
			time.sleep(30)
		except Exception as e:
			raise
getContent()