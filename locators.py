from selenium.webdriver.common.by import By


class CommonPageLocators:
    HEADER_LOGO = (By.ID, "header_logo")
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign in")
    LOG_OUT_LINK = (By.LINK_TEXT, "Sign out")


class LoginPageLocators:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    SIGN_IN_BUTTON = (By.ID, "SubmitLogin")


class HomePageLocators:
    QUICK_VIEW_BUTTON = (By.LINK_TEXT, 'Quick view')
    FIRST_PRODUCT = (By.XPATH, '//a[img[@title="Faded Short Sleeve T-shirts"]]')
    SECOND_PRODUCT = (By.XPATH, '//a[img[@title="Blouse"]]')
    PRODUCT_QUICK_VIEW_IFRAME = (By.XPATH, "//iframe[starts-with(@id,'fancybox-frame')]")
    DISPLAY_PRICE = (By.ID, "our_price_display")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@title="Continue shopping"]')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@title="Proceed to checkout"]')
    ADD_TO_CART_BUTTON = (By.ID, "add_to_cart")


class CheckoutPageLocators:
    FIRST_ITEM_PRICE = (By.XPATH, "//table/tbody/tr[1]/td[4]")
    SECOND_ITEM_PRICE = (By.XPATH, "//table/tbody/tr[2]/td[4]")
    SHIPPING_PRICE = (By.ID, "total_shipping")
    TOTAL_PRODUCTS_PRICE = (By.ID, "total_product")
    TOTAL_ORDER_PRICE = (By.ID, "total_price_container")
    FIRST_ITEM_ATTRIBUTES = (By.XPATH, "//table/tbody/tr[1]/td[2]/small[2]")
    SECOND_ITEM_ATTRIBUTES = (By.XPATH, "//table/tbody/tr[2]/td[2]/small[2]")

    PROCEED_TO_CHECKOUT_BUTTON_T1 = (By.LINK_TEXT, 'Proceed to checkout')
    PROCEED_TO_CHECKOUT_BUTTON_T3 = (By.NAME, 'processAddress')
    CHECK_BOX_TOS = (By.ID, 'uniform-cgv')
    PROCEED_TO_CHECKOUT_BUTTON_T4 = (By.NAME, 'processCarrier')
    PAY_BY_BANK_WIRE = (By.XPATH, "//a[@title='Pay by bank wire']")
    CONFIRM_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button')
