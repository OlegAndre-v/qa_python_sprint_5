from data import test_user_data


class TestProfileToConstructor:
    def test_navigate_from_profile_page_to_constructor_page_click_constructor_button(self, login_page, main_page, profile_page):
        login_page.open()
        login_page.login(test_user_data()['email'], test_user_data()['password'])
        main_page.click_profile_button()
        profile_page.click_constructor_button()
        assert main_page.get_order_button_text() == 'Оформить заказ'

    def test_navigate_from_profile_page_to_constructor_page_click_stellar_burgers_button(self, login_page, main_page, profile_page):
        login_page.open()
        login_page.login(test_user_data()['email'], test_user_data()['password'])
        main_page.click_profile_button()
        profile_page.click_stellar_burgers_button()
        assert main_page.get_order_button_text() == 'Оформить заказ'
