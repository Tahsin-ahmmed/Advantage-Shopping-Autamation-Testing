class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.username = "input[name='usernameRegisterPage']"
        self.email = "input[name='emailRegisterPage']"
        self.password = "input[name='passwordRegisterPage']"
        self.confirm_password = "input[name='confirm_passwordRegisterPage']"
        self.first_name = "input[name='first_nameRegisterPage']"
        self.last_name = "input[name='last_nameRegisterPage']"
        #self.phone = "input[name='phonenumberRegisterPage']"
        self.country = "select[name='countryListboxRegisterPage']"
        self.city = "input[name='cityRegisterPage']"
        self.address = "input[name='addressRegisterPage']"
        #self.state = "input[name='state/province/_regionRegisterPage']"
        #self.postal_code = "input[name='postal_codeRegisterPage']"
        self.agree_checkbox = "input[name='i_agree']"
        self.register_button = self.page.get_by_role("button", name="REGISTER")

        # Error locators
        self.user_exists_error = self.page.locator("text=User name already exists")
        self.email_error = self.page.locator("css=label[for='emailRegisterPage'] + * span")
        self.password_error = self.page.locator("css=label[for='passwordRegisterPage'] + * span")

    def register(self, user_data):
        self.page.fill(self.username, user_data["username"])
        self.page.fill(self.email, user_data["email"])
        self.page.fill(self.password, user_data["password"])
        self.page.fill(self.confirm_password, user_data["password"])
        self.page.fill(self.first_name, user_data["first_name"])
        self.page.fill(self.last_name, user_data["last_name"])
        #self.page.fill(self.phone, user_data["phone"])
        self.page.select_option(self.country, label=user_data["country"])
        self.page.fill(self.city, user_data["city"])
        self.page.fill(self.address, user_data["address"])
        #self.page.fill(self.state, user_data["state"])
        #self.page.fill(self.postal_code, user_data["postal_code"])
        self.page.check(self.agree_checkbox)
        self.register_button.click()
    
    def register1(self, user_data):
        self.page.fill(self.username, user_data["username"])
        self.page.fill(self.email, user_data["email"])
        self.page.fill(self.password, user_data["password"])
        self.page.fill(self.confirm_password, user_data["password"])
        self.page.fill(self.first_name, user_data["first_name"])
        self.page.fill(self.last_name, user_data["last_name"])
        #self.page.fill(self.phone, user_data["phone"])
        self.page.select_option(self.country, label=user_data["country"])
        self.page.fill(self.city, user_data["city"])
        self.page.fill(self.address, user_data["address"])
        #self.page.fill(self.state, user_data["state"])
        #self.page.fill(self.postal_code, user_data["postal_code"])
        self.page.check(self.agree_checkbox)
        #self.register_button.click()

    def is_user_exists_error_visible(self):
        return self.user_exists_error.is_visible()

    def is_email_error_visible(self):
        return self.email_error.is_visible()

    def is_password_error_visible(self):
        return self.password_error.is_visible()