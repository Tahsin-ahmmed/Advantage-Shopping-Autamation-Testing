from pages.login_page import LoginPage
from utils.data_loader import load_login_data
import os

def test_login_valid_user(page):
    data = load_login_data()["valid_user"]
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(data["username"], data["password"])

    page.wait_for_timeout(3000)  # Replace with a better wait if possible

    # Save storage state to file
    storage_path = os.path.join(os.path.dirname(__file__), '../../storage/login_storage.json')
    page.context.storage_state(path=storage_path)

    assert page.url == "https://advantageonlineshopping.com/#/"

    #assert page.locator("#menuUserLink").inner_text() == data["username"]


