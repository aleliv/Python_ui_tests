import pytest

from final.pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.should_be_login_link()


@pytest.mark.unique_tests
class TestProductSearch:
    def test_valid_product_search(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        search = "work"
        page.open()
        page.search_product(search=search)
        # Assert
        page.should_be_search_result()

    def test_not_valid_product_search(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        search = "u@*$HRQ_)H"
        page.open()
        page.search_product(search=search)
        # Assert
        page.should_be_search_result()
