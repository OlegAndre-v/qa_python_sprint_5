class TestUserLogin:
    def test_login_from_base_page_click_login_button(self, browser, base_page, login_page, test_user_data):
        base_page.open()
        base_page.click_login_button()
        login_page.login(test_user_data['email'], test_user_data['password'])
        assert base_page.get_order_button_text() == 'Оформить заказ'

    def test_login_from_base_page_click_profile_button(self, browser, base_page, login_page, test_user_data):
        base_page.open()
        base_page.click_profile_button()
        login_page.login(test_user_data['email'], test_user_data['password'])
        assert base_page.get_order_button_text() == 'Оформить заказ'

    def test_login_from_registration_page_click_login_button(self, browser, base_page, registration_page, login_page, test_user_data):
        registration_page.open()
        registration_page.click_login_button()
        login_page.login(test_user_data['email'], test_user_data['password'])
        assert base_page.get_order_button_text() == 'Оформить заказ'

    def test_login_from_forgot_password_page_click_login_button(self, browser, base_page, forgot_password_page, login_page, test_user_data):
        forgot_password_page.open()
        forgot_password_page.click_login_button()
        login_page.login(test_user_data['email'], test_user_data['password'])
        assert base_page.get_order_button_text() == 'Оформить заказ'
