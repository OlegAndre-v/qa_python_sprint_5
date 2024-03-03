from selenium.webdriver.common.by import By


class MainPageLocators:  # Стартовая страница
    LOGIN_BUTTON = (By.XPATH, './/button[text() = "Войти в аккаунт"]')  # Кнока "Войти в аккаунт"
    PROFILE_BUTTON = (By.XPATH, './/p[text() = "Личный Кабинет"]')  # Кнопка "Личный Кабинет"
    ORDER_BUTTON = (By.XPATH, './/button[text() = "Оформить заказ"]')  # Кнопка "Оформить заказ"
    BUN_BUTTON = (By.XPATH, './/span[text() = "Булки"]')  # Кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, './/span[text() = "Соусы"]')  # Кнопка "Соусы"
    TOPPING_BUTTON = (By.XPATH, './/span[text() = "Начинки"]')  # Кнопка "Начинки"
    BUN_SECTION = (By.XPATH, './/h2[text() = "Булки"]')  # Секция "Булки"
    SAUCES_SECTION = (By.XPATH, './/h2[text() = "Соусы"]')  # Секция "Соусы"
    TOPPING_SECTION = (By.XPATH, './/h2[text() = "Начинки"]')  # "Секция "Начинки"


class LoginPageLocators:  # Страница логина
    LOGIN_BUTTON = (By.XPATH, './/button[text() = "Войти"]')  # Кнопка "Войти"
    REGISTRATION_BUTTON = (By.XPATH, './/a[text() = "Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    EMAIL_INPUT = (By.XPATH, './/input[@name = "name"]')  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, './/input[@name = "Пароль"]')  # Поле "Пароль"


class RegistrationPageLocators:  # Страница регистрации
    NAME_INPUT = (By.XPATH, '(.//input[@name = "name"])[1]')  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, '(.//input[@name = "name"])[2]')  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, '(.//input[@name = "Пароль"])')  # Поле "Пароль"
    REGISTRATION_BUTTON = (By.XPATH, './/button[text() = "Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, './/a[text() = "Войти"]')  # Кнопка "Войти"
    INCORRECT_PASSWORD_ERROR = (By.XPATH, './/p[text() = "Некорректный пароль"]')  # Ошибка логина


class ProfilePageLocators:  # Страница "Личный кабинет"
    NAME_INPUT = (By.XPATH, './/input[@name = "Name"]')  # Поле "Имя"
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text() = "Конструктор"]')  # Кнопка "Конструктор"
    STELLAR_BURGERS_BUTTON = (By.XPATH, './/div[@class = "AppHeader_header__logo__2D0X2"]')  # Кнопка "Stellar Burgers"


class ForgotPasswordPageLocators:  # Страница "Востановление пароля"
    LOGIN_BUTTON = (By.XPATH, './/a[text() = "Войти"]')  # Кнопка "Войти"
