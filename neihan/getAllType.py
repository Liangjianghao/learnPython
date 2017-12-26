# coding:utf-8

# CREATE TABLE `neihanTable` (
#   `Id` int(11) NOT NULL AUTO_INCREMENT,
#   `create_time` datetime DEFAULT NULL COMMENT '创建时间',
#   `category_name` varchar(255) DEFAULT NULL COMMENT '类别名',
#   `category_id` int(11) DEFAULT NULL COMMENT '类别ID',
#   `follow_number` int(11) DEFAULT NULL COMMENT '订阅数',
#   `post_number` int(11) DEFAULT NULL COMMENT '帖子数',
#   `detail` varchar(255) DEFAULT NULL COMMENT '简介',
#   PRIMARY KEY (`Id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='内涵总表';

import requests
import os
import sys
import json
import pymysql
import datetime
reload(sys)
sys.setdefaultencoding('utf8')
def insertChatContent(category_name,category_id,follow_number,post_number,detail):
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
	if "'" in detail:
	 	detail=detail.replace("'","''")
	 	
	sql = "INSERT INTO neihanTable (create_time,category_name,category_id,follow_number,post_number,detail) VALUES ( '%s', '%s', '%s','%s','%s','%s')"  
	data = (createtime,category_name,category_id,follow_number,post_number,detail)
	print sql%data
	cursor.execute(sql % data)  
	connect.commit()   


url='http://is.snssdk.com/2/essay/discovery/v3/?iid=12316421155&os_version=10.1.1&os_api=18&live_sdk_version=220&channel=App%20Store&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.1'
response=requests.get(url).content
dic=json.loads(response)

category_list= dic['data']['categories']['category_list']
print len(category_list)
for category in category_list:
	insertChatContent(category['name'],category['id'],category['subscribe_count'],category['total_updates'],category['intro'])
