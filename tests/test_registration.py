from helpers import generate_login, generate_password, generate_incorrect_password
from elements import *
from data import test_user_data


class TestUserRegistration:
    def test_registration_user(self, browser, login_page, registration_page):
        login = generate_login()
        password = generate_password()
        registration_page.open()
        registration_page.fill_registration_form(test_user_data()['name'], login, password)
        login_page.login(login, password)
        assert browser.find_element(*MainPageLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_incorrect_password_error(self, browser, registration_page):
        registration_page.open()
        registration_page.fill_registration_form(test_user_data()['name'], generate_login(), generate_incorrect_password())
        error_message = 'Некорректный пароль'
        assert browser.find_element(*RegistrationPageLocators.INCORRECT_PASSWORD_ERROR).text == error_message
