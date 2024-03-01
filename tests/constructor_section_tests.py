class TestConstructorSection:
    def test_bulki_section_navigation(self, base_page):
        base_page.open()
        base_page.click_sous_button()
        base_page.click_bulki_button()
        assert base_page.get_bulki_section_text() == 'Булки'

    def test_sous_section_navigation(self, base_page):
        base_page.open()
        base_page.click_sous_button()
        assert base_page.get_sous_section_text() == 'Соусы'

    def test_nachinki_section_navigation(self, base_page):
        base_page.open()
        base_page.click_nachinki_button()
        assert base_page.get_nachinki_section_text() == 'Начинки'
