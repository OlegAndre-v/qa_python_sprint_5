class TestConstructorSection:
    def test_bun_section_navigation(self, main_page):
        main_page.open()
        main_page.click_sauces_button()
        main_page.click_bun_button()
        assert main_page.get_bun_section_text() == 'Булки'

    def test_sauces_section_navigation(self, main_page):
        main_page.open()
        main_page.click_sauces_button()
        assert main_page.get_sauces_section_text() == 'Соусы'

    def test_topping_section_navigation(self, main_page):
        main_page.open()
        main_page.click_topping_button()
        assert main_page.get_topping_section_text() == 'Начинки'
