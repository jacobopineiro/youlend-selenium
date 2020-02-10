from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import BasePage


class LoginPage(BasePage):
    # This class contains the actions needed in the login page
    def login_with_credentials(self, email_text, passwd_text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL)).send_keys(
            email_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD)).send_keys(
            passwd_text)
        super().click(LoginPageLocators.SIGN_IN_BUTTON)
