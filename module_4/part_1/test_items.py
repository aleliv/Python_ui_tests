def test_add_to_cart_button_name(browser):
    # Data
    page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    add_to_cart_button_name = 'Добавить в корзину'
    assertion_error_text = "The add to cart button's text is wrong"

    add_to_cart_button_locator = ".btn-add-to-basket"

    # Arrange
    browser.get(page_link)

    # Act
    search_add_to_cart_button = browser.find_element_by_css_selector(add_to_cart_button_locator)

    # Assert
    add_to_cart_button_text = search_add_to_cart_button.text
    assert add_to_cart_button_text == add_to_cart_button_name, assertion_error_text
