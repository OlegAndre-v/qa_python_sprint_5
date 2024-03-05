import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.profile_page import ProfilePage
from pages.forgot_password_page import ForgotPasswordPage


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(browser):
    base_url = "https://stellarburgers.nomoreparties.site/"
    return MainPage(browser, base_url)


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
