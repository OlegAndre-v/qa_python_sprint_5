from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements import *


class MainPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url_path=''):
        url = self.base_url + url_path
        self.driver.get(url)

    def click_login_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON))
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def click_profile_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.PROFILE_BUTTON))
        self.driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

    def get_order_button_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        return self.driver.find_element(*MainPageLocators.ORDER_BUTTON).text

    def click_bun_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.BUN_BUTTON))
        self.driver.find_element(*MainPageLocators.BUN_BUTTON).click()

    def get_bun_section_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.BUN_SECTION))
        return self.driver.find_element(*MainPageLocators.BUN_SECTION).text

    def click_sauces_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_BUTTON))
        self.driver.find_element(*MainPageLocators.SAUCES_BUTTON).click()

    def get_sauces_section_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.SAUCES_SECTION))
        return self.driver.find_element(*MainPageLocators.SAUCES_SECTION).text

    def click_topping_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.TOPPING_BUTTON))
        self.driver.find_element(*MainPageLocators.TOPPING_BUTTON).click()

    def get_topping_section_text(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.TOPPING_SECTION))
        return self.driver.find_element(*MainPageLocators.TOPPING_SECTION).text
