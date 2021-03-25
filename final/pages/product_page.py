from final.pages.base_page import BasePage
from final.pages.locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_product_btn.click()

    def should_be_add_product_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_MESSAGE_NAME).text, "No product added"

    def should_basket_cost_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRICE_MESSAGE).text, "Wrong price"

    def should_not_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), "Success message is " \
                                                                                          "present"

    def should_disappear_success_msg(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_SUCCESS_MESSAGE), "Success message is disappeared"

    def should_product_be_in_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket is empty"
