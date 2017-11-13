# coding:utf-8

# CREATE TABLE `moshuTable` (
#   `Id` int(11) NOT NULL AUTO_INCREMENT,
#   `create_time` datetime DEFAULT NULL COMMENT '创建时间',
#   `content_type` varchar(255) DEFAULT NULL COMMENT '类型',
#   `content` varchar(255) DEFAULT NULL COMMENT '内容',
#   `url` varchar(255) DEFAULT NULL COMMENT '网址',
#   PRIMARY KEY (`Id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='内涵魔术表';
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
def insertChatContent(create_time,content_type,content,url):
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
	sql = "INSERT INTO moshuTable (create_time,content_type,content,url) VALUES ( '%s', '%s', '%s','%s')"  
	print sql
	# create_time = pymysql.escape_string(create_time)
	# print create_time
	# content_type = pymysql.escape_string(content_type)
	savecontent = pymysql.escape_string(content)
	downUrl = pymysql.escape_string(url)
	data = (createtime,content_type,savecontent,downUrl)  
	print data
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')


def getDateUnix():
	return time.mktime(datetime.datetime.now().timetuple())
def getUrl():
	# return 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=10483316536&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%%20Store&device_platform=iphone&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&live_sdk_version=174&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&device_id=30277977392&aid=7&content_type=-102&count=30&double_col_mode=0&essence=1&latitude=31.08946115076879&longitude=121.5034942973322&message_cursor=175514038&min_time=%s&mpic=1'%(getDateUnix())
	return 'http://lf.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=244&count=30&level=6&message_cursor=175514038&min_time=%s&mpic=1&video_cdn_first=1'%(getDateUnix())
	# return 'http://lf.snssdk.com/neihan/stream/category/data/v2/?tag=joke&iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1&category_id=184&count=30&level=6&message_cursor=175514038&min_time=%s&mpic=1&video_cdn_first=1'%(getDateUnix())
print getUrl()	
def getContent():
	while True:
		try:
			url=getUrl()
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
									insertChatContent(joker['group']['create_time'],joker['group']['digg_count'],content,joker['group']['download_url'])
							# bury_count 踩 comment_count 评论 share_count 转发 
							# share_url for 101
			time.sleep(30)
		except Exception as e:
			raise
getContent()