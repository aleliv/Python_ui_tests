from module_5.pages.base_page import BasePage
from module_5.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are present"

    def should_be_empty_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Empty msg is not present"
