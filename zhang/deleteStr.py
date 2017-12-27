
# -- coding: UTF-8 -- 
import time
import sys
import os
with open('zhang.txt', 'r') as f:  
    data = f.readlines() 
for zhanghao in data:
	print zhanghao.strip()