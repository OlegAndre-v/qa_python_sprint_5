from data import *


class TestProfilePage:
    def test_navigate_from_base_page_to_profile(self, login_page, main_page, profile_page):
        login_page.open()
        login_page.login(test_user_data()['email'], test_user_data()['password'])
        main_page.click_profile_button()
        assert profile_page.get_profile_name() == test_user_data()['name']
