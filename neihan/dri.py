# coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
#百度搜索设置下拉框操作
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

#进入搜索设置页
# shezhi=driver.find_elements_by_class_name('pf')[1]
shezhi=driver.find_element_by_xpath('//*[@id="u1"]/a[8]')

ActionChains(driver).move_to_element(shezhi).perform()

driver.find_element_by_class_name('setpref').click()