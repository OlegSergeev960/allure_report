import allure
from selenium.webdriver.common.by import By

@allure.epic("Authorization")
@allure.feature("Authorization via password")
@allure.title("Вход с помощью валидных логина и пароля")
@allure.description("Успешная авторизация")
def test_successful_login(driver, valid_credentials):
    driver.get("https://the-internet.herokuapp.com/login")
    username, password = valid_credentials

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

    success_message = driver.find_element(By.CLASS_NAME, "flash.success").text
    assert "You logged into a secure area!" in success_message

@allure.epic("Authorization")
@allure.feature("Authorization via password")
@allure.title("Вход с помощью невалидных логина и пароля")
@allure.description("Неуспешная авторизация")
def test_unsuccessful_login(driver, invalid_credentials):
    driver.get("https://the-internet.herokuapp.com/login")
    username, password = invalid_credentials

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

    error_message = driver.find_element(By.CLASS_NAME, "flash.error").text

    assert "Your username is invalid!" in error_message