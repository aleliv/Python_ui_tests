import time

import pytest

from final.pages.login_page import LoginPage


class TestUserRegistration:
    @pytest.mark.personal_tests
    def test_new_user_registration(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        pswd = "QWERTY!@#$%"
        page = LoginPage(browser, link)
        # Act
        page.open()
        page.register_new_user(email=email, password=pswd)
        # Assert
        page.should_be_success_register_msg()

    @pytest.mark.unique_tests
    @pytest.mark.personal_tests
    def test_login(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        pswd = "QWERTY!@#$%"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email=email, password=pswd)
        page.user_logout()
        # Act
        page.go_to_login_page()
        page.user_login(email=email, password=pswd)
        # Assert
        page.should_be_success_login_msg()

    @pytest.mark.unique_tests
    def test_account_deleting(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        pswd = "QWERTY!@#$%"
        page = LoginPage(browser, link)
        # Act
        page.open()
        page.register_new_user(email=email, password=pswd)
        page.go_to_account_page()
        page.delete_account(password=pswd)
        # Assert
        page.should_be_success_del_msg()
        page.should_not_be_authorized_user()
