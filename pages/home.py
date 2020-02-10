from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base import BasePage


class HomePage(BasePage):
    # This class contains the actions needed in the home page and product iframe
    def quick_view_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
        super().click(HomePageLocators.QUICK_VIEW_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            HomePageLocators.PRODUCT_QUICK_VIEW_IFRAME))

    def get_price_quick_view(self):
        price = float(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            HomePageLocators.DISPLAY_PRICE)).text[1:])
        return price

    def add_to_cart_click(self):
        super().click(HomePageLocators.ADD_TO_CART_BUTTON)

    def continue_shopping_click(self):
        super().click(HomePageLocators.CONTINUE_SHOPPING_BUTTON)

    def proceed_to_checkout_click(self):
        super().click(HomePageLocators.PROCEED_TO_CHECKOUT_BUTTON)

    # For future versions, implement EC for the following to avoid using time.sleep()
    # Locator: SIZE_SELECTOR = (By.ID, "group_1")
    def change_item_size(self, size):
        select = Select(self.driver.find_element_by_id("group_1"))
        select.select_by_visible_text(size)

    def get_size_quick_view(self):
        select = Select(self.driver.find_element_by_id("group_1"))
        size = select.first_selected_option.text
        return size
