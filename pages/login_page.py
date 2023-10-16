import allure
from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.main_page import MainPage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._login = page.get_by_placeholder("Введите логин")
        self._password = page.get_by_placeholder("Введите пароль")
        self._submit = page.get_by_role("button", name="Войти")
        self._warning = page.get_by_role('dialog')
        self._warning_OK = page.get_by_role("button", name="ОК")
        self._main_page = MainPage(page)

    @property
    def main_page(self):
        return self._main_page

    @allure.step('Убеждаемся в наличии полей ввода логина и пароля')
    def check_presence_login_and_password_fields(self):
        expect(self._login, 'Поле Логин не отображается на странице').to_be_visible()
        expect(self._password, 'Поле Пароль не отображается на странице').to_be_visible()

    @allure.step('Заполняем поле логин юзера {username}')
    def enter_username(self, username: str):
        self._login.fill(username)

    @allure.step('Заполняем поле пароль')
    def enter_password(self, password: str):
        self._password.fill(password)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_submit(self):
        self._submit.click()

    @allure.step('Проверяем появление диалогового окна о вводе неверных логина или пароля')
    def check_presence_warning(self):
        expect(self._warning, 'Отсутствует диалоговое окно о вводе неверных логина или пароля.').to_be_visible()
        assert 'Неверное имя пользователя или пароль.' in self._warning.inner_text()
        self._warning_OK.click()

    @allure.step('Проходим аутентификацию для юзера {username}')
    def auth(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
