from src.domain.user import User
from src.pages.LoginPage import LoginPage


def test_admin_can_logout():
    admin = User("tomsmith", "SuperSecretPassword!")
    LoginPage() \
        .open() \
        .login_as(admin) \
        .logout()
