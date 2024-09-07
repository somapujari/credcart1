from selenium.webdriver.common.by import By


class Register:
    register_link_xpath = By.XPATH, "//a[text()= 'Register']"
    name_input_id = By.ID, 'name'
    email_input_id = By.ID, 'email'
    password_input_id = By.ID, 'password'
    conform_password_input_id = By.ID, 'password-confirm'
    register_btn_xpath = By.XPATH, "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def register_link_click(self):
        self.driver.find_element(*self.register_link_xpath).click()

    def name_enter(self, name):
        self.driver.find_element(*self.name_input_id).clear()
        self.driver.find_element(*self.name_input_id).send_keys(name)

    def email_enter(self, email):
        self.driver.find_element(*self.email_input_id).clear()
        self.driver.find_element(*self.email_input_id).send_keys(email)

    def password_enter(self, password):
        self.driver.find_element(*self.password_input_id).clear()
        self.driver.find_element(*self.password_input_id).send_keys(password)

    def confirm_pass_enter(self, password):
        self.driver.find_element(*self.conform_password_input_id).clear()
        self.driver.find_element(*self.conform_password_input_id).send_keys(password)

    def register_btn_click(self):
        self.driver.find_element(*self.register_btn_xpath).click()






