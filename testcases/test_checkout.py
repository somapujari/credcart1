from pageobjects.loginpageobj import Login
from pageobjects.select_product import Product_select
from pageobjects.checkouut_pageobj import Checkout
from utility.loggs import LogGen


class Test_Checkout:
    first_name = 'soma'
    last_name = 'pujari'
    phone = '8805633666'
    address = 'umadi maharashtra  416413'
    zip_code = '411039'
    state = 'Pune'
    owner_name = 'soma pujari'
    cvv = '123'
    card_number = '5299920000000149'
    year = 2024
    month = 'April'
    logger = LogGen.loggen()

    def test_checkout(self, setup):
        self.logger.info("test_checkout started")
        self.driver = setup
        self.logger.info('opening url')
        self.driver.get('https://automation.credence.in/shop')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.rg = Login(self.driver)
        self.logger.info('click on login link ')
        self.rg.login_link_click()
        self.logger.info('entering a password')
        self.rg.email_enter('soma123@gmail.com')
        self.logger.info('entering a password')
        self.rg.password_enter('Test@123')
        self.logger.info('click on  log in_ button')
        self.rg.login_button_click()
        self.rg.verify_login()
        self.pr = Product_select(self.driver)
        self.logger.info('click on product')
        self.pr.product_click()
        self.logger.info('adding to cart')
        self.pr.add_to_cart()
        self.pr.verify_added_cart()
        self.pr.checkout_clik()
        self.ck = Checkout(self.driver)
        self.logger.info('entering first_name')
        self.ck.first_name_enter(self.first_name)
        self.ck.last_name_enter(self.last_name)
        self.ck.phone_enter(self.phone)
        self.ck.address_enter(self.address)
        self.ck.zip_enter(self.zip_code)
        self.logger.info('entering state')
        self.ck.state_select(self.state)
        self.logger.info('entering owner name ')
        self.ck.owner_card_name_enter(self.owner_name)
        self.logger.info('entering cvv')
        self.ck.cvv_enter(self.cvv)
        self.ck.card_number_enter(self.card_number)
        self.ck.year_select(self.year)
        self.logger.info('entering month')
        self.ck.month_select(self.month)
        self.logger.info('click on checkout')
        self.ck.continue_checkout()

        try:
            self.logger.info('switch to alert')
            value = self.driver.switch_to.alert
            print(value.text)
            self.logger.info('reading alert message', value.text)
            self.driver.switch_to.alert.accept()
        except Exception as E:
            print(E)
            print('alert is not present')
        self.logger.info('verifying the order')
        self.ck.verify_order()
        self.logger.info('test_checkout is completed')
        print('the test is completed')
