import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    page.get_by_role("link", name="SpeakersCategory", exact=True).click()
    page.get_by_role("paragraph").filter(has_text="$269.99").click()
    page.get_by_role("button", name="ADD TO CART").click()
    page.locator("a[ng-click*=\"redirect('/category/'\"]", has_text="SPEAKERS").click()
    page.get_by_text("Bose SoundLink Wireless").click()
    page.get_by_role("button", name="ADD TO CART").click()
    page.get_by_role("link", name="ShoppingCart").click()
    page.get_by_role("cell", name="$129.00", exact=True).locator("div").nth(1).click()
    page.get_by_role("button", name="CHECKOUT ($269.99)").click()
    page.locator("input[name=\"usernameInOrderPayment\"]").click()
    page.locator("input[name=\"usernameInOrderPayment\"]").fill("TAHSIN")
    page.locator("#orderPayment label").filter(has_text=re.compile(r"^Password$")).click()
    page.locator("input[name=\"passwordInOrderPayment\"]").fill("TAHSIN222")
    page.get_by_role("button", name="LOGIN").click()
    page.locator("input[name=\"usernameInOrderPayment\"]").click()
    page.locator("input[name=\"usernameInOrderPayment\"]").fill("Tahsin")
    page.locator("input[name=\"passwordInOrderPayment\"]").click()
    page.locator("input[name=\"passwordInOrderPayment\"]").fill("Tahsin222")
    page.get_by_role("button", name="LOGIN").click()
    page.goto("https://advantageonlineshopping.com/#/orderPayment")
    page.get_by_role("button", name="NEXT").click()
    page.locator("label").filter(has_text="SafePay username").click()
    page.locator("input[name=\"safepay_username\"]").fill("Tahsin")
    page.locator("label").filter(has_text="SafePay password").click()
    page.locator("input[name=\"safepay_password\"]").fill("helloA1")
    page.locator("#pay_now_btn_SAFEPAY").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)