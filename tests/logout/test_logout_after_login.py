from pages.logout_page import LogoutPage

def test_user_can_logout(page):
    logout = LogoutPage(page)

    logout.navigate()
    logout.login("Tahsin", "Tahsin222")
    logout.logout()

    #assert logout.is_logged_out()
