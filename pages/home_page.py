class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/")

    def click_special_offer(self):
        self.page.get_by_role("link", name="SPECIAL OFFER").click()

    def click_popular_items(self):
        self.page.get_by_role("link", name="POPULAR ITEMS").click()

    def click_contact_us(self):
        self.page.get_by_role("link", name="CONTACT US").click()
