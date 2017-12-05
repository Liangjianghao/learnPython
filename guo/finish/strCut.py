# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import re
longstr=' 2010高清 小曲儿串烧(郭德纲 陶阳).mp3'
print len(longstr)
# shortStr=longstr.strip()
# shortStr=longstr.split(' ')[2]
resultStr=''
for index,NameStr in enumerate(longstr.split(' ')):
	if index==0 or index==1:
		continue
	else:
		resultStr+=NameStr
# print resultStr
# print len(resultStr)
# print resultStr.split('.')[0]

def cutStr(name):
	resultStr=''
	if ' ' in name :
		print 'come'
		for index,NameStr in enumerate(name.split(' ')):
			if index==0:
				continue
			else:
				resultStr+=NameStr
	# print resultStr
	else:
		resultStr=name
	resultStr=resultStr.split('.')[0]
	resultStr=resultStr.replace('（','').replace('）','').replace('《','').replace('》',' ')
	resultStr=re.sub(r"[\t,^\d{n}]",'',resultStr)
	return resultStr

print cutStr('2008《大实话》（郭德纲、张文顺）.mp3')	
s = "***+++\tabc***---\tdef**---\t**82008《大实话》（郭德纲、张文顺）.mp3"
s2=re.sub(r"[\*,\t,\-,\+,^\d{n}]","",s)
# # s2=s.replace("*",'').replace('-','').replace('+','').replace('\t','')
print s2

# path=path.strip()
# # 去除尾部 \ 符号
# path=path.rstrip("\\")