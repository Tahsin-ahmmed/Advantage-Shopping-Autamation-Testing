from pages.home_page import HomePage

def test_popular_items_clickable(page):
    home = HomePage(page)
    home.navigate()
    home.click_popular_items()
    # Optional: add assertions if target page is confirmed
