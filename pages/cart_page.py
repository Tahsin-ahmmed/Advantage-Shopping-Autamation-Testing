# pages/cart_page.py

class CartPage:
    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.get_by_role("link", name="ShoppingCart").click()

    def get_cart_item_count(self):
        return self.page.locator("#menuCart span").inner_text()

    def remove_item_by_price(self, price_text):
        self.page.get_by_role("cell", name=price_text, exact=True).locator("div").nth(1).click()
