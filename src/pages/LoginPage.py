from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.SecureAreaPage import SecureArea


class LoginPage(object):
    def __init__(self):
        self.username_input = s("#username")
        self.password_input = s("#password")
        self.login_btn = s("#login > button")

    def open(self):
        browser.open_url("/login")
        return self

    def login_as(self, user):
        self.username_input.set(user.name)
        self.password_input.set(user.password)
        self.login_btn.click()
        return SecureArea()
