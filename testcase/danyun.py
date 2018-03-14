import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class Testbaidu(unittest.TestCase):
    URL="http://www.baidu.com"
    locator_kw=(By.ID,'kw')
    locator_su=(By.ID,'su')
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.URL)
    def tearDown(self):
        self.driver.quit()
    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
