from pageobjects.select_product import Product_select
from pageobjects.loginpageobj import Login


class Test_Product:

    def test_product_select(self, setup):
        self.driver = setup
        self.driver.get('https://automation.credence.in/shop')
        self.rg = Login(self.driver)
        self.rg.login_link_click()
        self.rg.email_enter('soma123@gmail.com')
        self.rg.password_enter('Test@123')
        self.rg.login_button_click()
        self.rg.verify_login()
        self.pr = Product_select(self.driver)
        self.pr.product_click()
        self.pr.add_to_cart()
        self.pr.verify_added_cart()
        self.pr.checkout_clik()





