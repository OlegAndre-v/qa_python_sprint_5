Проект по тестированию https://stellarburgers.nomoreparties.site/.
Тесты находятся в директории tests
    -registration_tests # набор тестов регистрации пользователя
        test_registration_user - Тест на успешную регистрацию пользователя
        test_incorrect_password_error - Тест на наличие ошибки при вводе пароля менее 6 символов
    -login_tests # набор тестов логина пользователя
        test_login_from_base_page_click_login_button - Тест логина через кнопку "Войти в аккаунт" на стартовой странице
        test_login_from_base_page_click_profile_button - Teст логина через кнопку "Личный кабинет" на стартовой странице
        test_login_from_registration_page_click_login_button - Тест логина через кнопку "Войти" на странице регистрации
        test_login_from_forgot_password_page_click_login_button - Тест логина через кнопку "Войти" на странице восстановленя пароля
    -profile_navigation_tests # набор тестов по навигации в личный кабинет
        test_navigate_from_base_page_to_profile - Тест навигации в личный кабинет со стартовой страницы через кнопку "Личный кабинет"
    -constructor_section_tests # набор тестов по навигации в конструктор
        test_navigate_from_profile_page_to_constructor_page_click_constructor_button - Тест навигации в конструктор из личного кабинета через кнопку "Констуктор"
        test_navigate_from_profile_page_to_constructor_page_click_stellar_burgers_button - Тест навигации в конструктор из личного кабинета через кнопку "Stellar Burgers"
    -constructor_section_tests # набор тестов по навигации в секции конструктор
        test_bulki_section_navigation - Тест навигации до секции "Булки" через кнопку "Булки"
        test_sous_section_navigation - Тест навигации до сексии "Соусы" через кнопку "Соусы"
        test_nachinki_section_navigation - Тест навигации до секции "Начинки" через кнопку "Начинки"
    -conftest # содержит фикстуры для тестов
    -elements # содержит локаторы для тестов(локаторы подписаны)
    -pages-* # папка содержит файлы страниц с функциями необходимыми для тестов