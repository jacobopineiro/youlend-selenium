import os
import unittest
import time
from selenium import webdriver
from pages.base import BasePage
from pages.home import HomePage
from pages.login import LoginPage
from pages.checkout import CheckoutPage
from locators import CommonPageLocators, HomePageLocators, CheckoutPageLocators
from credentials import email, password
import HtmlTestRunner


class AutomationPracticeTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headeless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://automationpractice.com/')

    def test_TC001_purchase_two_items(self):
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # Step 0: Login:
        base_page.click(CommonPageLocators.SIGN_IN_LINK)
        login_page.login_with_credentials(email, password)
        base_page.click(CommonPageLocators.HEADER_LOGO)

        # Step 1: Quick View an item:
        home_page.quick_view_click(HomePageLocators.FIRST_PRODUCT)
        time.sleep(10)

        # Step 2: Change size of the item:
        home_page.change_item_size('L')

        # Step 3: Add item to basket (and store values for future asserts):
        first_item_size_quickview = home_page.get_size_quick_view()
        first_item_price_quickview = home_page.get_price_quick_view()
        home_page.add_to_cart_click()

        # Step4: Continue shopping:
        home_page.continue_shopping_click()

        # Step 5: Quick View different item (and store values for future asserts):
        home_page.quick_view_click(HomePageLocators.SECOND_PRODUCT)
        time.sleep(10)
        second_item_size_quickview = home_page.get_size_quick_view()
        second_item_price_quickview = home_page.get_price_quick_view()

        # Step 6: Add item to basket:
        home_page.add_to_cart_click()

        # Step 7, assert basket content:
        home_page.proceed_to_checkout_click()
        first_item_price_checkout = checkout_page.get_price_cart(CheckoutPageLocators.FIRST_ITEM_PRICE)
        second_item_price_checkout = checkout_page.get_price_cart(CheckoutPageLocators.SECOND_ITEM_PRICE)
        shipping_price = checkout_page.get_price_cart(CheckoutPageLocators.SHIPPING_PRICE)
        total_products = checkout_page.get_price_cart(CheckoutPageLocators.TOTAL_PRODUCTS_PRICE)
        total_order = checkout_page.get_price_cart(CheckoutPageLocators.TOTAL_ORDER_PRICE)

        assert first_item_size_quickview == checkout_page.get_size_cart(CheckoutPageLocators.FIRST_ITEM_ATTRIBUTES)
        assert second_item_size_quickview == checkout_page.get_size_cart(CheckoutPageLocators.SECOND_ITEM_ATTRIBUTES)

        assert first_item_price_quickview == first_item_price_checkout
        assert second_item_price_quickview == second_item_price_checkout

        # quantities rounded to 2 decimals when added to avoid floating point operation error:
        assert total_products == round(first_item_price_quickview+second_item_price_checkout, 2)
        assert total_order == round(total_products+shipping_price, 2)

        # Step 8: Proceed through checkout and complete by wire
        checkout_page.click_proceed_checkout_button_tab1()
        checkout_page.click_proceed_checkout_button_tab3()
        checkout_page.click_text_box_tos()
        checkout_page.click_proceed_checkout_button_tab4()
        checkout_page.click_on_pay_by_bank_wire()
        checkout_page.click_confirm_order()

        # Logout
        base_page.click(CommonPageLocators.LOG_OUT_LINK)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    curr_dir = os.getcwd()
    path = os.path.join(curr_dir, 'output')
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=path))
