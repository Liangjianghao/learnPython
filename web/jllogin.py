# -- coding: UTF-8 -- 
import time
import sys
import requests 
import os
import os.path
import chargeAlert

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
import pytesseract
import getstring
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def getCode():
	return getstring.getString()
def login(driver):
	sharp_img=Image.open("/Users/l/Desktop/img/image_code.png")
	code=pytesseract.image_to_string(sharp_img)
	print(code)

	# code=getstring.getString()
	# if code:
	elemCode = driver.find_element_by_id("Text_Login_VerCode")
	# elemCode.send_keys(code)
	elemCode.send_keys(code)
	elemCode.send_keys(Keys.RETURN)
	# time.sleep(3)
	
	result=chargeAlert.alert_is_present()(driver)
	print result
	if result:
		print'验证失败'
		result.accept()
		driver.close()
		result=False
		login(driver)

	else:
		print '验证成功'
		time.sleep(3)
		guajiBtn = driver.find_element_by_id("A_Menu_Run").click()
		jifen = driver.find_element_by_id("TD_Run_Score")
		guajishu=driver.find_element_by_id("Span_Run_OnNum")
		guajishuT=driver.find_element_by_id("Span_Run_MaxNum")
		print zhanghao+'--积分：'+jifen.text+'--在线:'+guajishu.text
		fo.write(zhanghao+'--积分：'+jifen.text+'--在线:'+guajishu.text)
		driver.close()

def getNumberOfJingling(zhanghao):
	

	driver = webdriver.Chrome()
	driver.get("http://vip.ipjingling.com/")
	elem = driver.find_element_by_id("Text_Login_EMail")
	elem.send_keys(zhanghao)
	# print zhanghao
	elem = driver.find_element_by_id("Text_Login_Pwd")
	elem.send_keys("123456")

	driver.get_screenshot_as_file('/Users/l/Desktop/screen/image.png')#比较好理解
	im =Image.open('/Users/l/Desktop/screen/image.png')
	box = (915,260,975,290)  #设置要裁剪的区域
	region = im.crop(box)     #此时，region是一个新的图像对象。
	region.save("/Users/l/Desktop/img/image_code.png")
	# region.show()#显示的话就会被占用，所以要注释掉
	# driver.close()

	im=Image.open("/Users/l/Desktop/img/image_code.png")
	imgry = im.convert('L')#图像加强，二值化
	sharpness =ImageEnhance.Contrast(imgry)#对比度增强
	sharp_img = sharpness.enhance(2.0)
	sharp_img.save("/Users/l/Desktop/img/image_code.png")
	# time.sleep(3)


	login(driver)
	# code=pytesseract.image_to_string(sharp_img)
	# print(code)

	# # code=getstring.getString()
	# # if code:
	# elemCode = driver.find_element_by_id("Text_Login_VerCode")
	# # elemCode.send_keys(code)
	# elemCode.send_keys(code)
	# elemCode.send_keys(Keys.RETURN)
	# # time.sleep(3)
	
	# result=chargeAlert.alert_is_present()(driver)
	# if result:
	# 	print'验证失败'
	# 	result.accept()
	# 	driver.close()
	# 	getNumberOfJingling(zhanghao)
	# else:


	# # al = driver.switch_to_alert()
	
	# # if al:
	# # 	print'验证失败'
	# # 	al.accept()
	# # 	driver.close()
	# # 	getNumberOfJingling(zhanghao)
	# # else:
	# 	time.sleep(3)
	# 	guajiBtn = driver.find_element_by_id("A_Menu_Run").click()
	# 	jifen = driver.find_element_by_id("TD_Run_Score")
	# 	guajishu=driver.find_element_by_id("Span_Run_OnNum")
	# 	guajishuT=driver.find_element_by_id("Span_Run_MaxNum")
	# 	print zhanghao+'--积分：'+jifen.text+'--在线:'+guajishu.text
	# 	fo.write(zhanghao+'--积分：'+jifen.text+'--在线:'+guajishu.text)
	# 	driver.close()

with open('zh.txt', 'r') as f:  
    data = f.readlines()  #txt中所有字符串读入data
# print data
path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
fo=open('%s/jl.txt'%(path),'w')
for zhanghao in data:
	# print zhanghao.strip()
	getNumberOfJingling(zhanghao.strip())
fo.close()
# driver.close()

