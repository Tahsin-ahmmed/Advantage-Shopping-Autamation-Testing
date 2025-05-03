import re
class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/")

    def go_to_speaker_product(self, product_name):
        self.page.get_by_role("link", name="SpeakersCategory", exact=True).click()
        self.page.get_by_text(product_name).click()

    def add_to_cart(self):
        self.page.get_by_role("button", name="ADD TO CART").click()

    def checkout(self):
        self.page.get_by_role("button", name=re.compile(r"^CHECKOUT")).click()


    def login_during_checkout(self, username, password):
        self.page.locator("input[name='usernameInOrderPayment']").fill(username)
        self.page.locator("input[name='passwordInOrderPayment']").fill(password)
        self.page.get_by_role("button", name="LOGIN").click()

    def click_next_on_payment(self):
        #self.page.locator("#next_btn").click()
        self.page.get_by_role("button", name="NEXT").first.click()

    def pay_with_safepay(self):
        self.page.locator("#pay_now_btn_SAFEPAY").click()
