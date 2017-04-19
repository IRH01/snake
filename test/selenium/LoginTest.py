#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


##
##需要下载chromedriver.exe放到python目录下面
##
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://uat.tsh365.cn/views/home.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_creat(self):
        driver = self.driver
        driver.get(self.base_url + "/views/login.html")
        driver.find_element_by_id("loginName").clear()
        driver.find_element_by_id("loginName").send_keys("admin")
        driver.find_element_by_id("passWord").clear()
        driver.find_element_by_id("passWord").send_keys("1234567")
        driver.find_element_by_id("denglu").click()
        # driver.find_element_by_xpath("//div[@id='menu']/div/ul/li[17]/div").click()
        # driver.find_element_by_link_text(u"优惠券·零售").click()
        # driver.get("http://uwmhlq.tsh365.cn/views/coupon/couponlist.html?roletype=1&btype=b2c")
        # driver.find_element_by_id("createCoupon").click()
        # driver.find_element_by_css_selector("input.textbox-text.validatebox-text").clear()
        # driver.find_element_by_css_selector("input.textbox-text.validatebox-text").send_keys("test234")
        # driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        # driver.find_element_by_xpath("//tr[4]/td[3]").click()
        # driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        # driver.find_element_by_xpath("//div[3]/div/div/div/div[2]/table/tbody/tr[4]/td[3]").click()
        # driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        # driver.find_element_by_xpath("//div[4]/div/div/div/div[2]/table/tbody/tr[4]/td[3]").click()
        # driver.find_element_by_xpath("//form[@id='addcoupon']/table/tbody/tr[6]/td[2]/span[2]/span/a").click()
        # driver.find_element_by_xpath("//div[5]/div/div/div/div[2]/table/tbody/tr[4]/td[3]").click()
        # driver.find_element_by_id("moneyType_0_1").click()
        # driver.find_element_by_xpath("(//label[@value='1'])[4]").click()
        # driver.find_element_by_xpath("(//input[@type='text'])[12]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys("1")
        # driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        # driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        # driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("5")
        # driver.find_element_by_id("submitForm").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
