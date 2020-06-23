from selene.support.conditions.have import text

from src.domain.user import User
from src.pages.LoginPage import LoginPage


def test_admin_can_login():
    admin = User("tomsmith", "SuperSecretPassword!")
    LoginPage() \
        .open() \
        .login_as(admin) \
        .logo.should_have(text("Secure Area"))
