from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Test_Prac:

    def __init__(self, driver):
        self.driver = driver

    def test_1(self):
        driver = webdriver.Chrome()
        driver.get('https://testautomationpractice.blogspot.com/')
        driver.execute_script('window.scrollBy(0,100)', "")
        driver.find_element(By.ID, 'name').send_keys('soma')

        # element = driver.find_element(By.ID, 'friday')
        # driver.execute_script('arguments[0].scrollIntoView()', element)
        driver.execute_script('window.scrollBy(0, document.body.scrollHeight())')
        time.sleep(4)

    def test_2(self):
        driver = webdriver.Chrome()
        driver.find_element(By.ID,  '')


