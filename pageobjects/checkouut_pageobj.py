from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Checkout:
    first_name_input_id = (By.ID, 'first_name')
    last_name_input_id = (By.ID, 'last_name')
    phone_input_id = (By.ID, 'phone')
    address_input_id = (By.ID, 'address')
    zip_input_id = (By.ID, 'zip')
    state_id_dropdown = (By.ID, 'state')
    owner_name_id = (By.ID, 'owner')
    cvv_input_id = (By.ID, 'cvv')
    card_number_input_id = (By.ID, 'cardNumber')
    year_select_id = (By.ID, 'exp_year')
    month_select_id = (By.ID, 'exp_month')
    continue_checkout_id = (By.ID, 'confirm-purchase')
    verify_order_xpath = (By.XPATH, "//div[@class='container text-center']/p[contains(text(),'Your order has been placed successfully')]")

    def __init__(self, driver):
        self.driver = driver

    def first_name_enter(self, first_name):
        self.driver.find_element(*self.first_name_input_id).send_keys(first_name)

    def last_name_enter(self, last_name):
        self.driver.find_element(*self.last_name_input_id).send_keys(last_name)

    def phone_enter(self, phone):
        self.driver.find_element(*self.phone_input_id).clear()
        self.driver.find_element(*self.phone_input_id).send_keys(phone)

    def address_enter(self, address):
        self.driver.find_element(*self.address_input_id).send_keys(address)

    def zip_enter(self, zip_code):
        self.driver.find_element(*self.zip_input_id).clear()
        self.driver.find_element(*self.zip_input_id).send_keys(zip_code)

    def state_select(self, state):
        ele = self.driver.find_element(*self.state_id_dropdown)
        ele.click()
        # drop = Select(ele)
        # options = drop.options
        # for option in options:
        #     if option == state:
        #         option.click()
        #         break
        self.driver.find_element(By.XPATH, f"//select[@id='state']//option[contains(text(),'{state}')]").click()

    def owner_card_name_enter(self, owner_name):
        self.driver.find_element(*self.owner_name_id).clear()
        self.driver.find_element(*self.owner_name_id).send_keys(owner_name)

    def cvv_enter(self, cvv):
        self.driver.find_element(*self.cvv_input_id).clear()
        self.driver.find_element(*self.cvv_input_id).send_keys(cvv)

    def card_number_enter(self, card_number):
        self.driver.find_element(*self.card_number_input_id).clear()
        for i in range(0,len(card_number), 4):
            chunk = card_number[i:i+4]
            self.driver.find_element(*self.card_number_input_id).send_keys(chunk)

    def year_select(self, year):
        self.driver.find_element(*self.year_select_id).click()
        # year_op = self.driver.find_elements(By.XPATH, '//select[@id="exp_year"]/option')
        # for option in range(1, len(year_op)+1):
        #     value = self.driver.find_element(By.XPATH, '//select[@id="exp_year"]/option')
        #     if value.text == year:
        #         value.click()
        #         break
        self.driver.find_element(By.XPATH, f"//select[@id = 'exp_year']/option[contains(text(),'{year}')]").click()

    def month_select(self, month):
        month_se = self.driver.find_element(*self.month_select_id)
        month_se.click()
        drop = Select(month_se)
        drop.select_by_visible_text(month)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_checkout_id).click()

    # def verify_order(self):
    #     ver = self.driver.find_element(*self.verify_order_xpath)
    #     ver1 = ver.is_displayed()
    #     print(ver1)
    #     try:
    #         if ver.text == 'Your order has been placed successfully.':
    #             assert True
    #             print('saving  the  screenshot')
    #             self.driver.save_screenshot(r"C:\Users\Dell\PycharmProjects\crecartproject1\screenshot\checkot_pass.jpg")
    #         else:
    #             self.driver.save_screenshot(r"C:\Users\Dell\PycharmProjects\crecartproject1\screenshot\screen_fail_check_out.jpg")
    #             assert False
    #     except Exception as E:
    #         print(E)
    def verify_order(self):
        try:
            # Find the element and check if it is displayed
            ver = self.driver.find_element(*self.verify_order_xpath)
            ver1 = ver.is_displayed()
            print(f"Element displayed: {ver1}")

            # Check the text of the element
            if ver.text == 'Your order has been placed successfully.':
                print('Order verified successfully.')
                # Save screenshot for success
                self.driver.save_screenshot(
                    r"C:\Users\Dell\PycharmProjects\crecartproject1\screenshot\checkot_pass.png")
            else:
                print('Order verification failed.')
                # Save screenshot for failure
                self.driver.save_screenshot(
                    r"C:\Users\Dell\PycharmProjects\crecartproject1\screenshot\screen_fail_check_out.png")
                assert False, 'Order verification failed.'

        except Exception as e:
            # Print the exception message and save screenshot
            print(f"An error occurred: {e}")
            self.driver.save_screenshot(r"C:\Users\Dell\PycharmProjects\crecartproject1\screenshot\error_check_out.png")
            assert False, f"Exception occurred: {e}"


