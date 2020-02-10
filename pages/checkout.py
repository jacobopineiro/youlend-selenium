from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import BasePage
from locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    # This class contains the actions needed in the checkout page
    def get_price_cart(self, by_locator):
        price = float(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text[1:])
        return price

    def get_size_cart(self, by_locator):
        attributes_string = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        attributes_dict = dict(r.split(' : ') for r in attributes_string.split(', '))
        return attributes_dict['Size']

    def click_proceed_checkout_button_tab1(self):
        super().click(CheckoutPageLocators.PROCEED_TO_CHECKOUT_BUTTON_T1)

    def click_proceed_checkout_button_tab3(self):
        super().click(CheckoutPageLocators.PROCEED_TO_CHECKOUT_BUTTON_T3)

    def click_text_box_tos(self):
        super().click(CheckoutPageLocators.CHECK_BOX_TOS)

    def click_proceed_checkout_button_tab4(self):
        super().click(CheckoutPageLocators.PROCEED_TO_CHECKOUT_BUTTON_T4)

    def click_on_pay_by_bank_wire(self):
        super().click(CheckoutPageLocators.PAY_BY_BANK_WIRE)

    def click_confirm_order(self):
        super().click(CheckoutPageLocators.CONFIRM_ORDER)
