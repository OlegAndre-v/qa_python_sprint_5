from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..elements import *


class ProfilePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url_path=''):
        url = self.base_url + url_path
        self.driver.get(url)

    def click_constructor_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(ProfilePageLocators.NAME_INPUT))
        self.driver.find_element(*ProfilePageLocators.CONSTRUCTOR_BUTTON).click()

    def click_stellar_burgers_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(ProfilePageLocators.NAME_INPUT))
        self.driver.find_element(*ProfilePageLocators.STELLAR_BURGERS_BUTTON).click()

    def get_profile_name(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(ProfilePageLocators.NAME_INPUT))
        return self.driver.find_element(*ProfilePageLocators.NAME_INPUT).get_attribute('value')
