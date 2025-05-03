import os
from playwright.sync_api import sync_playwright
from pages.search_page import SearchPage

def test_search_exact_product_with_session():
    # Path to the saved session data (login_storage.json)
    storage_path = os.path.join(os.path.dirname(__file__), '../../storage/login_storage.json')

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=storage_path)  # Load saved session
        page = context.new_page()

        # Use the search page object to navigate and perform search
        search_page = SearchPage(page)
        search_page.navigate()
        search_page.search_product("HP ROAR WIRELESS SPEAKER")

        if page.url == "https://advantageonlineshopping.com/#/search/3?viewAll=HP%20ROAR%20WIRELESS%20SPEAKER":
            print("URL is correct")
        else:
            print("URL is incorrect" + page.url)

        
        context.close()
        browser.close()
