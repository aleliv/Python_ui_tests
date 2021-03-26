import time

import pytest

from final.pages.basket_page import BasketPage
from final.pages.login_page import LoginPage
from final.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", pytest.param("offer7", marks=pytest.mark.xfail), "offer8"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        promo_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
        page = ProductPage(browser, promo_link)
        # Act
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        page.should_be_add_product_message()
        page.should_basket_cost_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        link_city = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link_city)
        # Act
        page.open()
        page.go_to_basket_page()
        # Assert
        page.should_no_products()
        page.should_be_empty_msg()


@pytest.mark.personal_tests
class TestGuestAddToBasketFromProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, product_link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.should_be_add_product_message()
        page.should_basket_cost_message()

    @pytest.mark.unique_tests
    def test_product_in_basket(self, browser):
        # Arrange
        product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, product_link)
        page.open()
        # Act
        page.add_product_to_basket()
        page.go_to_basket_page()
        # Assert
        page.should_product_be_in_the_basket()
