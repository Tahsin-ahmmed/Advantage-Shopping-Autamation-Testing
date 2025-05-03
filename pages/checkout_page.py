class CheckoutPage:
    def __init__(self, page):
        self.page = page

    # Navigate to the homepage
    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/")

    # Go to the shopping cart page
    def go_to_cart(self):
        self.page.get_by_role("link", name="ShoppingCart").click()

    # Add a product to the cart by selecting its price
    def add_product_to_cart(self, price):
        self.page.locator("a[ng-click*=\"redirect('/category/'\"]", has_text="SPEAKERS").click()
        self.page.get_by_role("paragraph").filter(has_text=price).click()
        self.page.get_by_role("button", name="ADD TO CART").click()

    # Remove a product from the cart by price
    def remove_product_from_cart(self, price):
        self.page.get_by_role("cell", name=price, exact=True).locator("div").nth(1).click()

    # Proceed to checkout from the cart page
    def proceed_to_checkout(self, total_price_label):
        self.page.get_by_role("button", name=f"CHECKOUT ({total_price_label})").click()

    # Continue to the payment section after checkout
    def continue_to_payment(self):
        self.page.goto("https://advantageonlineshopping.com/#/orderPayment")
        self.page.get_by_role("button", name="NEXT").click()

    # Enter SafePay details and confirm the payment
    def enter_safepay_and_pay(self, safepay_username, safepay_password):
        self.page.locator("input[name=\"safepay_username\"]").fill(safepay_username)
        self.page.locator("input[name=\"safepay_password\"]").fill(safepay_password)
        self.page.locator("#pay_now_btn_SAFEPAY").click()
