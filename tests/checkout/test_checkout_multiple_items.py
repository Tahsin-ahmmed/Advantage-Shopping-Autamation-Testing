from playwright.sync_api import sync_playwright
from pages.checkout_page import CheckoutPage

def test_checkout_after_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        checkout = CheckoutPage(page)

        checkout.navigate()
        
        # Perform login manually
        page.get_by_label("UserMenu").get_by_title("USER").click()
        page.locator("input[name='username']").fill("Tahsin")
        page.locator("input[name='password']").fill("Tahsin222")
        page.get_by_role("button", name="SIGN IN").click()

        # Continue with checkout
        checkout.go_to_speaker_product("Bose Soundlink Bluetooth Speaker III")
        checkout.add_to_cart()
        checkout.checkout()
        checkout.click_next_on_payment()
        checkout.pay_with_safepay()

        context.close()
        browser.close()
