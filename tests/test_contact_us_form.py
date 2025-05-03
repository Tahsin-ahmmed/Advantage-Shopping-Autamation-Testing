from pages.contact_us_page import ContactUsPage

def test_contact_us_form_submission(page):
    contact = ContactUsPage(page)
    contact.navigate()
    contact.open_contact_us()
    contact.fill_contact_form(email="tasin@gmail.com", subject="Product issue")
    contact.submit_form()
    assert contact.is_submission_successful()
