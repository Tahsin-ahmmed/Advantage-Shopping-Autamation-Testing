from pages.registration_page import RegistrationPage
from utils.data_loader import load_registration_data

def test_existing_username_registration(page):
    page.goto("https://advantageonlineshopping.com/#/register")
    data = load_registration_data()["existing_username"]
    registration_page = RegistrationPage(page)
    registration_page.register(data)
    page.wait_for_timeout(3000)
    assert registration_page.is_user_exists_error_visible()
    assert page.locator("text=User name already exists").is_visible()


