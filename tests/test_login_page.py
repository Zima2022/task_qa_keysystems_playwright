import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from test_data import LOGIN, PASSWORD


class TestLoginPage:

    @pytest.mark.parametrize('login, password', [
        (LOGIN, '3'),
        ('wrong_login', PASSWORD),
        ('wrong_login', 'wrong_password')
    ])
    def test_login_page_wrong_credentials(self, page: Page, login: str, password: str):
        login_page = LoginPage(page)

        # Открытие страницы логирования
        login_page.open_page()

        # Проверка присутствия полей ввода логина и пароля
        login_page.check_presence_login_and_password_fields()

        # Ввод учетных данных и кликаем "Войти"
        login_page.enter_username(login)
        login_page.enter_password(password)
        login_page.click_submit()

        # Проверка появления диалогового окна с сообщением о неверном логине или пароле
        login_page.check_presence_warning()

    def test_login_page_right_credentials(self, page: Page):
        login_page = LoginPage(page)
        main_page = login_page.main_page

        # Открытие страницы логирования
        login_page.open_page()

        # Проверка присутствия полей ввода логина и пароля
        login_page.check_presence_login_and_password_fields()

        # Прохождение аутентификации с верными учетными данными
        login_page.auth(LOGIN, PASSWORD)

        # Выходим из системы
        main_page.log_out()
