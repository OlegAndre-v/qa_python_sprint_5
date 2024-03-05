# Проект по UI тестированию https://stellarburgers.nomoreparties.site/.
Автотесты для сервиса Stellar Burgers. Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.
## Файлы:
- tests/ - директрория с тестами.
  
    - test_registration - набор тестов регистрации пользователя
        - test_registration_user - Тест на успешную регистрацию пользователя
        - test_incorrect_password_error - Тест на наличие ошибки при вводе пароля менее 6 символов
    - test_login - набор тестов логина пользователя
        - test_login_from_base_page_click_login_button - Тест логина через кнопку "Войти в аккаунт" на стартовой странице
        - test_login_from_base_page_click_profile_button - Teст логина через кнопку "Личный кабинет" на стартовой странице
        - test_login_from_registration_page_click_login_button - Тест логина через кнопку "Войти" на странице регистрации
        - test_login_from_forgot_password_page_click_login_button - Тест логина через кнопку "Войти" на странице восстановленя пароля
    - test_profile_navigation - набор тестов по навигации в личный кабинет
        - test_navigate_from_base_page_to_profile - Тест навигации в личный кабинет со стартовой страницы через кнопку "Личный кабинет"
    - test_profile_to_constructor - набор тестов по навигации в конструктор
        - test_navigate_from_profile_page_to_constructor_page_click_constructor_button - Тест навигации в конструктор из личного кабинета через кнопку "Констуктор"
        - test_navigate_from_profile_page_to_constructor_page_click_stellar_burgers_button - Тест навигации в конструктор из личного кабинета через кнопку "Stellar Burgers"
    - test_constructor_section - набор тестов по навигации в секции конструктор
        - test_bun_section_navigation - Тест навигации до секции "Булки" через кнопку "Булки"
        - test_sauces_section_navigation - Тест навигации до сексии "Соусы" через кнопку "Соусы"
        - test_topping_section_navigation - Тест навигации до секции "Начинки" через кнопку "Начинки"
    -conftest - содержит фикстуры для тестов
- pages/ - набор методов для тестов
- data - набор тд
- elements - локаторы
- helpers - дополнительные методы

  ### Для запуска тестов должны быть установлены:
`pytest`
`selenium`
