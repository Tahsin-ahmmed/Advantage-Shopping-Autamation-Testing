class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/")
        #self.page.wait_for_timeout(30000)

    def open_contact_us(self):
        self.page.get_by_role("link", name="CONTACT US").wait_for_element_state("visible", timeout=30000)
        self.page.get_by_role("link", name="CONTACT US").click()

    def fill_contact_form(self, email, subject, category_value="object:60", product_value="object:124"):
        self.page.locator("select[name=\"categoryListboxContactUs\"]").select_option(category_value)
        #self.page.wait_for_timeout(30000)
        self.page.locator("select[name=\"productListboxContactUs\"]").wait_for_element_state("visible", timeout=30000)
        self.page.locator("select[name=\"productListboxContactUs\"]").select_option(product_value)
        self.page.locator("input[name=\"emailContactUs\"]").fill(email)
        self.page.locator("textarea[name=\"subjectTextareaContactUs\"]").fill(subject)

    def submit_form(self):
        self.page.get_by_role("button", name="SEND").click()

    def is_submission_successful(self):
        return self.page.locator("#registerSuccessCover").get_by_text(
            "Thank you for contacting Advantage shopping"
        ).is_visible()
