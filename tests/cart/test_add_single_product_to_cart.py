from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage

def test_add_single_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="storage/login_storage.json")
        page = context.new_page()

        cart_page = CartPage(page)

        page.goto("https://advantageonlineshopping.com/#/")
        page.get_by_role("link", name="SpeakersCategoryTxt").click()
        page.get_by_text("Bose Soundlink Bluetooth").click()
        page.get_by_role("button", name="ADD TO CART").click()

        cart_count = page.locator("#shoppingCartLink .cart").inner_text()
        assert cart_count == "1"

        context.close()
        browser.close()
