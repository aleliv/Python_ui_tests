from datetime import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url.__contains__("login"), "It is not login URL"
        assert True

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REG_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PSWD_REG_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PSWD_REG_FIELD_REP).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()
