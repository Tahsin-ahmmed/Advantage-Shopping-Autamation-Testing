from pages.login_page import LoginPage
from utils.data_loader import load_login_data

def test_login_blank_password(page):
    data = load_login_data()["invalid_users"][3]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login1(data["username"], data["password"])

    assert login_page.is_login_button_disabled(), "Login button should be disabled when password is blank"
