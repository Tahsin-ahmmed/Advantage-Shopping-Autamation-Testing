from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/")

    def login(self, username: str, password: str):
        self.page.get_by_label("UserMenu").get_by_title("USER").click()
        self.page.locator("input[name=\"username\"]").fill(username)
        self.page.locator("input[name=\"password\"]").fill(password)
        self.page.get_by_role("button", name="SIGN IN").click()

    def logout(self):
        self.page.get_by_label("UserMenu").get_by_title("USER").click()
        self.page.get_by_role("link", name="Sign out").click()

    def is_logged_out(self) -> bool:
        self.page.get_by_label("UserMenu").get_by_title("USER").click()
        return self.page.get_by_role("link", name="Sign in").is_visible()
