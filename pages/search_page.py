class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_icon = page.get_by_title("SEARCH")
        self.search_box = page.get_by_role("textbox", name="Search")

    def navigate(self):
        self.page.goto("https://advantageonlineshopping.com/#/")

    def search_product(self, product_name: str):
        self.search_icon.click()
        self.search_box.fill(product_name)
        self.search_box.press("Enter")
