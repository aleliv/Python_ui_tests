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

    def should_be_success_register_msg(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MSG), "Success message is not present"

    def user_logout(self):
        self.browser.find_element(*LoginPageLocators.LOGOUT_BTN).click(), "User is not logged in or wrong page"

    def user_login(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PSWD_LOGIN_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def should_be_success_login_msg(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MSG), "Success message is not present"

    def go_to_account_page(self):
        self.browser.find_element(*LoginPageLocators.ACCOUNT_LINK).click(), "User is not logged in"

    def delete_account(self, password):
        self.browser.find_element(*LoginPageLocators.DELETE_BTN).click()
        self.browser.find_element(*LoginPageLocators.PSWD_DEL_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.COMFIRM_DELETE_BTN).click()

    def should_be_success_del_msg(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_DEL_MSG), "Account is not deleted"


