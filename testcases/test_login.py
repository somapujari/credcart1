from pageobjects.loginpageobj import Login
from selenium import webdriver


class TestLogin:
    url = 'https://automation.credence.in/shop'
    email = 'soma123@gmail.com'
    password = 'Test@123'

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.rg = Login(self.driver)
        self.rg.login_link_click()
        self.rg.email_enter(self.email)
        self.rg.password_enter(self.password)
        self.rg.login_button_click()
        self.rg.verify_login()


