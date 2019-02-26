# -*- coding: utf-8 -*-
# @Time : 2019/1/14 11:27 
# @Author : for 
# @File : 02_seleium_test.py 
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.python.org')
# assert 'python' in driver.title
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('python')
elem.send_keys(Keys.RETURN)
# assert 'No results found' not in driver.page_source
driver.close()
