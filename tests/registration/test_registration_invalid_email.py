from pages.registration_page import RegistrationPage
from utils.data_loader import load_registration_data

def test_invalid_email_registration(page):
    page.goto("https://advantageonlineshopping.com/#/register")
    data = load_registration_data()["invalid_email"]
    registration_page = RegistrationPage(page)
    registration_page.register1(data)

    error_message = page.inner_text("label.animated.invalid")  # Using the class selector for the label
    assert error_message == "Your email address isn't formatted correctly"
