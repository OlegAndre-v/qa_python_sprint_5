import time
from .elements import *


class TestUserRegistration:
    def test_registration_user(self, browser, login_page, registration_page, profile_page, test_user_data, login_generator, password_generator):
        registration_page.open()
        registration_page.fill_registration_form(test_user_data['name'], login_generator, password_generator)
        time.sleep(1)
        login_page.login(login_generator, password_generator)
        assert browser.find_element(*BasePageLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_incorrect_password_error(self, browser, registration_page, test_user_data, login_generator, incorrect_password_generator):
        registration_page.open()
        registration_page.fill_registration_form(test_user_data['name'], login_generator, incorrect_password_generator)
        error_message = 'Некорректный пароль'
        assert browser.find_element(*RegistrationPageLocators.INCORRECT_PASSWORD_ERROR).text == error_message
