from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements import *


class RegistrationPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url_path=''):
        url = self.base_url + url_path
        self.driver.get(url)

    def click_login_button(self):
        self.driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()

    def fill_registration_form(self, name, login, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
        self.driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(login)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BUTTON))
