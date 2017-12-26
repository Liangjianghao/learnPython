# coding:utf-8
import os
def mkFile(path):	
	isExists=os.path.exists(path)
	if not isExists:
		os.makedirs(path)
		print path+'创建成功'
	else:
		print '目录已存在'