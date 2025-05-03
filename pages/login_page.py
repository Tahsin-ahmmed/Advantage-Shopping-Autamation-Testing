class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_menu = page.get_by_label("UserMenu").get_by_title("USER")
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.sign_in_button = page.get_by_role("button", name="SIGN IN")

    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/", timeout=20000)

    def login(self, username, password):
        self.user_menu.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.sign_in_button.click()

    def login1(self, username, password):
        self.user_menu.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        #self.sign_in_button.click()

    

    def is_login_button_disabled(self):
        return self.page.get_by_role("button", name="SIGN IN").get_attribute("disabled") is not None

