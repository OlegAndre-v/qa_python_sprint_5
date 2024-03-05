from data import user_data


class TestUserLogin:
    def test_login_from_base_page_click_login_button(self, main_page, login_page):
        main_page.open()
        main_page.click_login_button()
        login_page.login(user_data['email'], user_data['password'])
        assert main_page.get_order_button_text() == 'Оформить заказ'

    def test_login_from_base_page_click_profile_button(self, main_page, login_page):
        main_page.open()
        main_page.click_profile_button()
        login_page.login(user_data['email'], user_data['password'])
        assert main_page.get_order_button_text() == 'Оформить заказ'

    def test_login_from_registration_page_click_login_button(self, main_page, registration_page, login_page):
        registration_page.open()
        registration_page.click_login_button()
        login_page.login(user_data['email'], user_data['password'])
        assert main_page.get_order_button_text() == 'Оформить заказ'

    def test_login_from_forgot_password_page_click_login_button(self, main_page, forgot_password_page, login_page):
        forgot_password_page.open()
        forgot_password_page.click_login_button()
        login_page.login(user_data['email'], user_data['password'])
        assert main_page.get_order_button_text() == 'Оформить заказ'
