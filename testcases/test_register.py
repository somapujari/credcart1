import time
from pageobjects.register_pageobject import Register


class Test_Register:
    url = 'https://automation.credence.in/shop'
    name = 'soma'
    email = 'soma123@gmail.com'
    password = 'Test@123'

    def test_register(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.re = Register(self.driver)
        time.sleep(3)
        self.re.register_link_click()
        time.sleep(3)
        self.re.name_enter(self.name)
        self.re.email_enter(self.email)
        self.re.password_enter(self.password)
        self.re.confirm_pass_enter(self.password)
        self.re.register_btn_click()
        time.sleep(40)
