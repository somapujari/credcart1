from selenium.webdriver.common.by import By


class Login:
    login_link_xpath = (By.XPATH, "//a[text()='Login']")
    email_input_id = (By.ID, 'email')
    password_input_id = (By.ID, 'password')
    login_btn_xpath = (By.XPATH, "//button[@type='submit']")
    verify_xpath = (By.XPATH, '//h2')

    def __init__(self, driver):
        self.driver = driver

    def login_link_click(self):
        self.driver.find_element(*self.login_link_xpath).click()

    def email_enter(self, email):
        self.driver.find_element(*self.email_input_id).clear()
        self.driver.find_element(*self.email_input_id).send_keys(email)

    def password_enter(self, password):
        self.driver.find_element(*self.password_input_id).clear()
        self.driver.find_element(*self.password_input_id).send_keys(password)

    def login_button_click(self):
        self.driver.find_element(*self.login_btn_xpath).click()

    def verify_login(self):
        te = self.driver.find_element(*self.verify_xpath).text
        if 'CredKart' in te:
            assert True
        else:
            assert False
