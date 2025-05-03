from pages.login_page import LoginPage
from utils.data_loader import load_login_data

def test_login_blank_username(page):
    data = load_login_data()["invalid_users"][2]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login1(data["username"], data["password"])

    assert page.locator("#menuUserLink").inner_text() == ""
