from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_user_login():
    # Data
    login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"

    title_text = 'Войти или зарегистрироваться | Oscar - Sandbox'
    test_email = "testpochta@mail.ru"
    test_passwd = "Q!W@E#R$T%"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(login_page_link)

        wait_title = WebDriverWait(browser, 10)
        wait_title.until(EC.title_is(title_text))

        search_input_email = browser.find_element_by_name("login-username")
        search_input_passwd = browser.find_element_by_name("login-password")
        search_login_button = browser.find_element_by_name("login_submit")

        # Act
        search_input_email.send_keys(test_email)
        search_input_passwd.send_keys(test_passwd)
        search_login_button.click()

        # Assert
        result_alert = browser.find_element_by_css_selector("div.alertinner").text
        assert result_alert == "Рады видеть вас снова", "The user is not logged in"

    finally:
        browser.quit()


test_user_login()
