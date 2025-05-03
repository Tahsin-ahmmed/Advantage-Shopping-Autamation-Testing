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
        search_query = "$%#@"
        search_page.search_product(search_query)
        assert page.locator("span.ng-binding", has_text=f'No results for "{search_query}"').text_content().strip() == f'No results for "{search_query}"'

        # Assert the text is present on the page
        #assert "No search results found. However, you can extend your search through the new SAP user experience (uses SAPUI5)" in page.locator("label.ng-binding").text_content()

        
        context.close()
        browser.close()
