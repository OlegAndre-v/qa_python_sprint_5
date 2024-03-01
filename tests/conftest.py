import random
import string
import pytest
from selenium import webdriver
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.registration_page import RegistrationPage
from .pages.profile_page import ProfilePage
from .pages.forgot_password_page import ForgotPasswordPage


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def base_page(browser):
    base_url = "https://stellarburgers.nomoreparties.site/"
    return BasePage(browser, base_url)


@pytest.fixture(scope='function')
def login_page(browser):
    base_url = "https://stellarburgers.nomoreparties.site/login"
    return LoginPage(browser, base_url)


@pytest.fixture(scope='function')
def registration_page(browser):
    base_url = "https://stellarburgers.nomoreparties.site/register"
    return RegistrationPage(browser, base_url)


@pytest.fixture(scope='function')
def profile_page(browser):
    base_url = "https://stellarburgers.nomoreparties.site/account/profile"
    return ProfilePage(browser, base_url)


@pytest.fixture(scope='function')
def forgot_password_page(browser):
    base_url = "https://stellarburgers.nomoreparties.site/forgot-password"
    return ForgotPasswordPage(browser, base_url)


@pytest.fixture(scope='function')
def login_generator():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 10)))
    domains = ['yandex.ru', 'mail.ru', 'gmail.com', 'yahoo.com', 'hotmail.com']
    random_domain = random.choice(domains)
    email = f'test_{random_string}@{random_domain}'
    return email


@pytest.fixture(scope='function')
def password_generator():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 10)))
    return random_string


@pytest.fixture(scope='function')
def incorrect_password_generator():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 5)))
    return random_string


@pytest.fixture(scope='function')
def test_user_data():
    user_data = {
        'name': 'Oleg',
        'email': 'Oleg_Andreev_6_007@ya.ru',
        'password': '123123Aa',
    }
    return user_data
