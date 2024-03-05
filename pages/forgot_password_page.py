from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements import *


class ForgotPasswordPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, url_path=''):
        url = self.base_url + url_path
        self.driver.get(url)

    def click_login_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(ForgotPasswordPageLocators.LOGIN_BUTTON))
        self.driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()
