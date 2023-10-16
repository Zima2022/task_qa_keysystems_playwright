from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from test_data import DIRECTORIES


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._navigator = page.locator('#navigatorTree-body')
        self._content_daily_mode = page.locator('//div[@class="x-grid-scroll-container "]')
        self._close_tab_daily_mode = page.get_by_text(' Закрыть эту вкладку')
        self._tab_daily_mode = page.get_by_role('tab', name='Ежедневный')

    def log_out(self):
        self.page.get_by_role("button", name="Тестовый (trac_test)").click()
        self.page.get_by_role("menuitem", name="Выйти").click()
        self.page.get_by_role("button", name="Да", exact=True).click()

    def navigator_element(self, name: str):
        return self.page.get_by_role("gridcell", name=name)

    def check_navigator_has_required_directories(self):
        for directory in DIRECTORIES:
            expect(self.navigator_element(directory)).to_be_visible()

    def collapse_all_nodes_in_navigator(self):
        self._navigator.click(button='right')
        self.page.get_by_role("menuitem", name="Свернуть все узлы").click()

    def open_daily_mode(self):
        self.check_navigator_has_required_directories()
        self.navigator_element('УЧЕТ ВЫПОЛНЕННЫХ РАБОТ').dblclick()
        self.navigator_element('Ежедневный').dblclick()
        expect(self._tab_daily_mode).to_be_visible()
        expect(self._content_daily_mode).to_be_visible()

    def close_daily_mode(self):
        self._close_tab_daily_mode.click()
