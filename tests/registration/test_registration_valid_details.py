from pages.registration_page import RegistrationPage
from utils.data_loader import load_registration_data

def test_valid_registration(page):
    page.goto("https://advantageonlineshopping.com/#/register")
    data = load_registration_data()["valid_user"]
    registration_page = RegistrationPage(page)
    registration_page.register(data)
    page.wait_for_timeout(3000)
    assert not registration_page.is_user_exists_error_visible()