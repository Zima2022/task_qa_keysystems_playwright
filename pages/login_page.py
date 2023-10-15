from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.main_page import MainPage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._login = '#textfield-1018-inputEl'
        self._password = '#textfield-1019-inputEl'
        self._main_page = MainPage(page)

    @property
    def main_page(self):
        return self._main_page

    def check_presence_login_and_password_fields(self):
        expect(self.page.locator(self._login), 'Поле Логин не отображается на странице').to_be_visible()
        expect(self.page.locator(self._password), 'Поле Пароль не отображается на странице').to_be_visible()

    def enter_username(self, username: str):
        self.page.fill(self._login, username)

    def enter_password(self, password: str):
        self.page.fill(self._password, password)

    def click_submit(self):
        self.page.get_by_role("button", name="Войти").click()

    def check_presence_warning(self):
        dialog = self.page.get_by_role('dialog')
        expect(dialog, 'Отсутствует диалоговое окно о вводе неверных логина или пароля.').to_be_visible()
        assert 'Неверное имя пользователя или пароль.' in dialog.inner_text()
        self.page.get_by_role("button", name="ОК").click()

    def auth(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
