import time

from selenium import webdriver

# -Пользовательский сценарий 1.2
# Логин в личный кабинет
# --Тестовый сценарий 1.2.1
# Логин в личный кабинет
# Предусловия:
# Пользователь не залогинен

try:
    browser = webdriver.Chrome()

    # Открываем страницу логина
    browser.get("http://selenium1py.pythonanywhere.com/ru/accounts/login")

    # Проверяем, что находимся на нужной транице
    assert "Войти" in browser.title, "Открыта не страница авторизации"

    # Ввести зарегистрированный в системе адрес электронной почты
    inputemail = browser.find_element_by_name("login-username")
    inputemail.send_keys("testpochta@mail.ru")  # тестовый email

    # Ввести пароль в поле

    inputpswd = browser.find_element_by_name("login-password")
    inputpswd.send_keys("Q!W@E#R$T%")  # тестовый пароль

    # Нажать кнопку "Войти"

    button = browser.find_element_by_name("login_submit")
    button.click()

    # Проверяем успешный логин

    alert = browser.find_element_by_css_selector("div.alertinner").text
    assert alert == "Рады видеть вас снова", "Логин не произошел"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()
