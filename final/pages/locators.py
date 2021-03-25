from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "register_form")
    EMAIL_REG_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PSWD_REG_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PSWD_REG_FIELD_REP = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success")
    LOGOUT_BTN = (By.CSS_SELECTOR, "#logout_link")
    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    PSWD_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.NAME, "login_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR, "div#messages > :nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "div#messages > :nth-child(3) strong")
    PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > :nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BTN = (By.CSS_SELECTOR, ".navbar-right .btn.btn-default")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")
