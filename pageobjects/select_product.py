from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product_select:
    electronic_no_xpath = (By.XPATH, "//h3[contains(text(),'Electric Guitar')]")
    add_to_cart_xpath = (By.XPATH, "//input[@type='submit'and @value='Add to Cart']")
    add_cart_veri_xpath = (By.XPATH, '//div[@class="alert alert-success"]')
    checkout_xpath = (By.XPATH, '//a[@href="/checkout"]')

    def __init__(self, driver):
        self.driver = driver

    def product_click(self):
        self.driver.find_element(*self.electronic_no_xpath).click()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_xpath).click()

    def verify_added_cart(self):
        wait = WebDriverWait(self.driver, 10)
        ele = self.driver.find_element(*self.add_cart_veri_xpath)
        wait.until(EC.presence_of_element_located(self.add_cart_veri_xpath))

    def checkout_clik(self):
        self.driver.find_element(*self.checkout_xpath).click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Checkout form')]")))




