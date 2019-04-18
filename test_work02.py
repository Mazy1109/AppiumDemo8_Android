#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

"""
添加自选股，添加阿里巴巴股票，验证阿里巴巴已经在自主股中
"""

from appium import webdriver
from time import sleep

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "demo"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/open")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox")
el2.click()
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()
el4 = driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox")
el4.click()
el5 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el5.click()
sleep(5)
el6 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el7.send_keys("alibaba")
el8 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
el8.click()