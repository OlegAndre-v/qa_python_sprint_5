from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..elements import *


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url_path=''):
        url = self.base_url + url_path
        self.driver.get(url)

    def click_login_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.LOGIN_BUTTON))
        self.driver.find_element(*BasePageLocators.LOGIN_BUTTON).click()

    def click_profile_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.PROFILE_BUTTON))
        self.driver.find_element(*BasePageLocators.PROFILE_BUTTON).click()

    def get_order_button_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.ORDER_BUTTON))
        return self.driver.find_element(*BasePageLocators.ORDER_BUTTON).text

    def click_bulki_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.BULKI_BUTTON))
        self.driver.find_element(*BasePageLocators.BULKI_BUTTON).click()

    def get_bulki_section_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.BULKI_SECTION))
        return self.driver.find_element(*BasePageLocators.BULKI_SECTION).text

    def click_sous_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.SOUS_BUTTON))
        self.driver.find_element(*BasePageLocators.SOUS_BUTTON).click()

    def get_sous_section_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.SOUS_SECTION))
        return self.driver.find_element(*BasePageLocators.SOUS_SECTION).text

    def click_nachinki_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.NACHINKI_BUTTON))
        self.driver.find_element(*BasePageLocators.NACHINKI_BUTTON).click()

    def get_nachinki_section_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(BasePageLocators.NACHINKI_SECTION))
        return self.driver.find_element(*BasePageLocators.NACHINKI_SECTION).text
