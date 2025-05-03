from pages.registration_page import RegistrationPage
from utils.data_loader import load_registration_data

def test_invalid_password_registration(page):
    page.goto("https://advantageonlineshopping.com/#/register")
    data = load_registration_data()["invalid_password"]
    registration_page = RegistrationPage(page)
    registration_page.register(data)
    page.wait_for_timeout(3000)
    assert registration_page.is_password_error_visible()