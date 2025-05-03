from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage

def test_remove_item_from_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="storage/login_storage.json")
        page = context.new_page()

        cart_page = CartPage(page)

        page.goto("https://advantageonlineshopping.com/#/")
        page.get_by_role("link", name="SpeakersCategory", exact=True).click()
        page.get_by_role("paragraph").filter(has_text="$269.99").click()
        page.get_by_role("button", name="ADD TO CART").click()
        page.locator("a[ng-click*=\"redirect('/category/'\"]", has_text="SPEAKERS").click()
        page.get_by_text("Bose SoundLink Wireless").click()
        page.get_by_role("button", name="ADD TO CART").click()

        cart_count = page.locator("#shoppingCartLink .cart").inner_text()
        assert cart_count == "2"

        cart_page.open_cart()
        cart_page.remove_item_by_price("$129.00")

        cart_count = page.locator("#shoppingCartLink .cart").inner_text()
        assert cart_count == "1"

        context.close()
        browser.close()
