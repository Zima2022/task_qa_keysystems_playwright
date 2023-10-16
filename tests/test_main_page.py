from playwright.sync_api import Page

from pages.login_page import LoginPage
from test_data import LOGIN, PASSWORD


class TestMainPage:

    def test_navigator_has_required_directories(self, page: Page):
        login_page = LoginPage(page)
        main_page = login_page.main_page

        # Открытие страницы логирования
        login_page.open_page()

        # Прохождение аутентификации с верными учетными данными
        login_page.auth(LOGIN, PASSWORD)

        # Проверка наличия обязательных директорий в панели навигатора
        main_page.check_navigator_has_required_directories()

        # Выходим из системы
        main_page.log_out()

    def test_open_daily_mode(self, page: Page):
        login_page = LoginPage(page)
        main_page = login_page.main_page

        # Открытие страницы логирования
        login_page.open_page()

        # Прохождение аутентификации
        login_page.auth(LOGIN, PASSWORD)

        # Отрытие режима "Ежедневный"
        main_page.open_daily_mode()

        # Закрываем вкладку "Ежедневный" на рабочем столе
        main_page.close_daily_mode()

        # Выходим из системы
        main_page.log_out()
