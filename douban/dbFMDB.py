# coding:utf-8
import datetime
import time 
import requests
import json
import sys
import os
import pymysql
import sys
import urllib
import os.path

reload(sys)
sys.setdefaultencoding('utf8')
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'123456',
          'db':'douban',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
connection = pymysql.connect(**config)
try:
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql='SELECT * FROM douban.doubanMovieTable where uptime>2000  moviescore>9.5;'
        
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        # print(result)
        listResult=list(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

 
finally:
    connection.close();
print len(listResult) 
print listResult   

# for index,each in enumerate(result):
# 	category_name=each['category_name']
	# digg_count= str(int(each['digg_count'])/10000)+'k'
	# # print each['content']
	# # print each['comments']
	# path='/Volumes/my/test3/%s'%category_name
	# isExists=os.path.exists(path)

	# if not isExists:
	# 	os.makedirs(path)
	# 	print path+'创建成功'
	# else:
	# 	print '目录已存在'
	# downloadUrl=each['url']
	# comments=''
	# name=''
	# if each['comments']=='无神评':
	# 	print '无神评'
	# 	name=digg_count+'_'+each['content']
	# else:
	# 	comments=each['comments']
	# 	name=digg_count+'_'+each['comments']
	# print name
	# name=name.replace('/','')
	# path='%s/%s.mp4'%(path,name)
	# urllib.urlretrieve(downloadUrl, path)    



 
