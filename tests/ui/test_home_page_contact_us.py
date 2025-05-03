from pages.home_page import HomePage

def test_contact_us_clickable(page):
    home = HomePage(page)
    home.navigate()
    home.click_contact_us()
    # Optional: assert something like a contact form appears
