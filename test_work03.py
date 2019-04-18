#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-

"""
进去自选，点击搜索，搜索alibaba，点击添加。然后回到自选，判断阿里巴巴已经在自选中，
把测试用例代码贴到回复里。测试用例的名字 test_search_add
"""

from appium import webdriver
import pytest
import unittest


class TestXueqiu(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search_add(self):
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")

        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()
        self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        self.driver.find_element_by_id("action_close").click()

        assert 1 == len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id, 'portfolio_stockName') and @text='阿里巴巴']"))









