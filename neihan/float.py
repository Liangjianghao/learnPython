# coding:utf-8
from decimal import *
import json 
import time
# detail="You don't know love far high--法海你不懂爱。"
# print (detail)
# print detail[-2]
# if "'" in detail:
#  	print detail
#  	detail=detail.replace("'","''")
#  	print detail
strT='1231231231298'
# print strT[-3:-1]
numt=int(strT[-3:-1])+1
print numt
numt=str(numt)[-2] if numt%10==0 else str(numt)
print numt
# if numt%10==0:
# 	print numt
# dic={"max_time": 1513316455.8100019}

# print (dic['max_time'])
# print Decimal(dic['max_time'])
print (str(time.time()).split('.')[0])




