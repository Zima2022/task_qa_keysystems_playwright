import os

from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = os.getenv('URL')

    def open_page(self):
        self.page.goto(self.url)
