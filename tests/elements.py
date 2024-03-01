from selenium.webdriver.common.by import By


class BasePageLocators:  # Стартовая страница
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # Кнока "Войти в аккаунт"
    PROFILE_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')  # Кнопка "Личный кабинет"
    ORDER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # Кнопка "Оформить заказ"
    BULKI_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')  # Кнопка "Булки"
    SOUS_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')  # Кнопка "Соусы"
    NACHINKI_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')  # Кнопка "Начинки"
    BULKI_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')  # Секция "Булки"
    SOUS_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')  # Секция "Соусы"
    NACHINKI_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')  # "Секция "Начинки"


class LoginPageLocators:  # Страница логина
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка "Войти"
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')  # Кнопка "Зарегистрироваться"
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле "Пароль"


class RegistrationPageLocators:  # Страница регистрации
    NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')  # Поле "Пароль"
    REGISTRATION_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка "Войти"
    INCORRECT_PASSWORD_ERROR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')  # Ошибка логина


class ProfilePageLocators:  # Страница "Личный кабинет"
    NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/div/div/input')  # Поле "Имя"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')  # Кнопка "Конструктор"
    STELLAR_BURGERS_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')  # Кнопка "Stellar Burgers"


class ForgotPasswordPageLocators:  # Страница "Востановление пароля"
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка "Войти
