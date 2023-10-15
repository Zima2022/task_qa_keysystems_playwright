from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from test_data import DIRECTORIES


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._navigator = '#navigatorTree-body'

    def log_out(self):
        self.page.get_by_role("button", name="Тестовый (trac_test)").click()
        self.page.get_by_role("menuitem", name="Выйти").click()
        self.page.get_by_role("button", name="Да", exact=True).click()

    def check_navigator_has_required_directories(self):
        for directory in DIRECTORIES:
            expect(self.page.get_by_role("gridcell", name=directory)).to_be_visible()

    def collapse_all_nodes_in_navigator(self):
        self.page.locator(self._navigator).click(button='right')
        self.page.get_by_role("menuitem", name="Свернуть все узлы").click()
