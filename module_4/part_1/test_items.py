def test_add_to_cart_button_name(browser):
    # Data
    page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    assertion_error_text = "The add to cart button's text is wrong"
    add_to_cart_button_name = "Add to basket"
    add_to_cart_button_locator = ".btn-add-to-basket"

    # Arrange
    browser.get(page_link)

    if browser.current_url.__contains__("com/ru"):
        add_to_cart_button_name = 'Добавить в корзину'
    elif browser.current_url.__contains__("com/es"):
        add_to_cart_button_name = 'Añadir al carrito'
    elif browser.current_url.__contains__("com/fr"):
        add_to_cart_button_name = 'Ajouter au panier'

    # Act
    search_add_to_cart_button = browser.find_element_by_css_selector(add_to_cart_button_locator)

    # Assert
    add_to_cart_button_text = search_add_to_cart_button.text
    assert add_to_cart_button_text == add_to_cart_button_name, assertion_error_text
