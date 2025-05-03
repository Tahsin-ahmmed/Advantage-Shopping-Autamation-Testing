from pages.registration_page import RegistrationPage
from utils.data_loader import load_registration_data

def test_missing_email_registration(page):
    page.goto("https://advantageonlineshopping.com/#/register")
    data = load_registration_data()["missing_email"]
    registration_page = RegistrationPage(page)
    registration_page.register1(data)


    page.wait_for_timeout(3000)
    #assert registration_page.is_email_error_visible()

    error_text = page.locator("label.invalid", has_text="Email field is required").inner_text()
    assert error_text == "Email field is required"

