from time import sleep

import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from test_data import DIRECTORIES, LOGIN


class MainPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._navigator = page.locator('#navigatorTree-body')
        self._content_daily_mode = page.locator('//div[@class="x-grid-scroll-container "]')
        self._close_tab_daily_mode = page.get_by_text(' Закрыть эту вкладку')
        self._tab_daily_mode = page.get_by_role('tab', name='Ежедневный')
        self._desktop_toolbar = page.get_by_role('tabpanel').last
        self._user_account = page.get_by_role('button', name=f'Тестовый ({LOGIN})')
        self._quit = page.get_by_role('menuitem', name='Выйти')
        self._dialog_quit_OK = page.get_by_role('button', name='Да', exact=True)

    @allure.step('Проверяем загрузилась ли панель инструментов рабочего стола')
    def check_desktop_toolbar_is_visible(self):
        expect(self._desktop_toolbar).to_be_visible()

    @allure.step('Выполняем выход')
    def log_out(self):
        sleep(3)
        self._user_account.click()
        self._quit.click()
        self._dialog_quit_OK.click()

    def navigator_element(self, name: str):
        return self.page.get_by_role('gridcell', name=name)

    @allure.step('Проверяем наличие обязательных директорий на панели навигатора')
    def check_navigator_has_required_directories(self):
        for directory in DIRECTORIES:
            expect(self.navigator_element(directory)).to_be_visible()

    @allure.step('Сворачиваем все каталоги на панели навигатора')
    def collapse_all_nodes_in_navigator(self):
        self._navigator.click(button='right')
        self.page.get_by_role('menuitem', name='Свернуть все узлы').click()

    @allure.step('Открываем режим "Ежедневный"')
    def open_daily_mode(self):
        self.check_navigator_has_required_directories()
        self.navigator_element('УЧЕТ ВЫПОЛНЕННЫХ РАБОТ').dblclick()
        self.navigator_element('Ежедневный').dblclick()
        expect(self._tab_daily_mode).to_be_visible()
        expect(self._content_daily_mode).to_be_visible()

    @allure.step('Закрываем вкладку "Ежедневный" на рабочем столе')
    def close_daily_mode(self):
        self._close_tab_daily_mode.click()
