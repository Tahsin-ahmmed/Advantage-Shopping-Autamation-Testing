from pages.home_page import HomePage

def test_special_offer_clickable(page):
    home = HomePage(page)
    home.navigate()
    home.click_special_offer()
    # You can add assert here to verify navigation if needed
