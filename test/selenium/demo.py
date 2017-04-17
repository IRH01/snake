# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class Yhq(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome()
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver =  webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://uat.tsh365.cn/views/home.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_yhq(self):
        driver = self.driver
        # ERROR: Caught exception [unknown command [优惠券创建]]
        driver.get(self.base_url + "/views/home.html")
        driver.find_element_by_link_text(u"优惠券·零售").click()
        driver.find_element_by_id("createCoupon").click()
        driver.find_element_by_css_selector("input.textbox-text.validatebox-text").clear()
        driver.find_element_by_css_selector("input.textbox-text.validatebox-text").send_keys("34567")
        driver.find_element_by_css_selector("a.textbox-icon.combo-arrow").click()
        driver.find_element_by_xpath("//div[2]/table/tbody/tr[4]/td[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("//div[3]/div/div/div/div[2]/table/tbody/tr[4]/td[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("//div[4]/div/div/div/div[2]/table/tbody/tr[4]/td[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
        driver.find_element_by_xpath("//div[5]/div/div/div/div[2]/table/tbody/tr[4]/td[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("2")
        driver.find_element_by_id("submitForm").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("16")
        driver.find_element_by_id("submitForm").click()

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
