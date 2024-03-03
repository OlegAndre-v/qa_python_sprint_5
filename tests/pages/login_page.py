from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements import *


class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url_path=''):
        url = self.base_url + url_path
        self.driver.get(url)

    def click_registration_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.REGISTRATION_BUTTON))
        self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def login(self, login, password):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
