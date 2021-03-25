import time

import pytest

from final.pages.login_page import LoginPage


@pytest.mark.personal_tests
class TestUserRegistration:
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


