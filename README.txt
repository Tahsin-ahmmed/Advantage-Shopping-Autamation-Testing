
# Advantage Online Shopping E2E Automation Test Suite

This project contains an automated end-to-end (E2E) test suite for the Advantage Online Shopping website.
The tests are implemented using Playwright with Python and follow the Page Object Model (POM) for better maintainability and organization.

The suite covers a wide range of functionalities, such as user registration, login, logout, product search, cart operations, and checkout. It uses Playwright's sync API and pytest for test management and execution.

---

## TABLE OF CONTENTS

1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Running Tests](#running-tests)
5. [Fixtures](#fixtures)
6. [Test Organization](#test-organization)
7. [Technologies Used](#technologies-used)
8. [Test Categories](#test-categories)
9. [Best Practices](#best-practices)
10. [Contribution](#contribution)
11. [License](#license)

---

## PROJECT OVERVIEW

This project is designed to provide a comprehensive E2E test suite for the Advantage Online Shopping website. The website allows users to purchase electronic products, including laptops, tablets, and speakers. The tests validate the following core areas:

- **User Registration**: Ensure that valid and invalid user registration works as expected.
- **Login**: Test login functionality with valid, invalid, and empty credentials.
- **Search**: Verify that products can be searched and the correct results are returned.
- **Cart**: Validate that users can add, remove, and view products in the cart.
- **Checkout**: Test the checkout process with and without login, including payment options.
- **Logout**: Ensure that users can successfully log out of the website.
- **UI/UX**: Validate that key links and banners are clickable and visible.

The test suite is designed to be reusable, extensible, and organized for easy maintenance.

---

## PROJECT STRUCTURE

The following is the organization of the project:

```
project-root/
│
├── pages/                        # Page Object Model (POM) classes for each page
│   ├── cart_page.py              # Page actions for the cart page
│   ├── checkout_page.py          # Page actions for the checkout process
│   ├── contact_us_page.py        # Page actions for the "Contact Us" page
│   ├── home_page.py              # Page actions for the homepage
│   ├── login_page.py             # Page actions for the login page
│   ├── logout_page.py            # Page actions for the logout functionality
│   ├── registration_page.py      # Page actions for the registration page
│   └── search_page.py            # Page actions for the search functionality
│
├── tests/                        # Test cases organized by feature
│   ├── cart/                     # Cart-related tests
│   │   ├── test_add_multiple_products_to_cart.py
│   │   ├── test_add_single_product_to_cart.py
│   │   └── test_remove_item_from_cart.py
│   │
│   ├── checkout/                 # Checkout-related tests
│   │   ├── test_checkout_multiple_items.py
│   │   └── test_checkout_without_login.py
│   │
│   ├── login/                    # Login-related tests
│   │   ├── test_login_empty_password.py
│   │   ├── test_login_empty_username.py
│   │   ├── test_login_invalid_password.py
│   │   ├── test_login_invalid_username.py
│   │   └── test_login_valid_credentials.py
│   │
│   ├── logout/                   # Logout-related tests
│   │   └── test_logout_after_login.py
│   │
│   ├── registration/             # Registration-related tests
│   │   ├── test_registration_exiting_user.py
│   │   ├── test_registration_invalid_email.py
│   │   ├── test_registration_invalid_password.py
│   │   ├── test_registration_missing_email.py
│   │   └── test_registration_valid_details.py
│   │
│   ├── search/                   # Search-related tests
│   │   ├── test_search_empty_input.py
│   │   ├── test_search_exact_product.py
│   │   ├── test_search_partial_product.py
│   │   ├── test_search_special_characters.py
│   │   └── test_search_wrong_product.py
│   │
│   ├── ui/                       # UI/UX-related tests
│   │   ├── test_home_page_contact_us.py
│   │   ├── test_home_page_popular_items.py
│   │   └── test_home_page_special_offers.py
│   │
│   └── test_contact_us_form.py   # Test for the Contact Us form submission
│
├── conftest.py                   # Shared fixtures for Playwright browser and page
└── requirements.txt              # Python dependencies
```

---

## GETTING STARTED

To get started with this project, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/your-repository/advantage-shopping-e2e.git
cd advantage-shopping-e2e
```

### 2. Install dependencies:

Create a virtual environment (recommended) and install the required packages.

```bash
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scriptsctivate
pip install -r requirements.txt
```

### 3. Install Playwright browser binaries:

Playwright requires certain browser binaries for automation. You can install them by running the following command:

```bash
playwright install
```

---

## RUNNING TESTS

You can run all tests or specific tests based on your needs.

### 1. Run all tests:

```bash
pytest tests/
```

### 2. Run tests in a specific folder:

For example, to run all tests related to login:

```bash
pytest tests/login/
```

### 3. Run a specific test file:

```bash
pytest tests/cart/test_add_single_product_to_cart.py
```

### 4. Run tests with additional options:

You can run the tests with options like `-v` (verbose) or `--maxfail` to limit the number of failures.

Example:

```bash
pytest tests/ --maxfail=3 -v
```

---

## FIXTURES

The `conftest.py` file contains a shared `page` fixture that is used by all tests. This fixture initializes the browser and creates a new page with a fresh context before each test. It ensures that each test has an isolated environment.

### `page` Fixture:
- Launches a Chromium browser in headless mode (optional).
- Creates a new context and a page.
- Sets a default timeout of 10 seconds for actions.
- Closes the context and browser after the test is completed.

---

## TEST ORGANIZATION

The tests are organized by feature into separate folders:

- **cart**: Tests related to adding, removing, and viewing cart items.
- **checkout**: Tests covering the checkout process with and without login.
- **login**: Tests for login functionality with different invalid and valid cases.
- **logout**: Tests to ensure proper logout functionality.
- **registration**: Tests for user registration functionality.
- **search**: Tests for the product search functionality.
- **ui**: Tests for verifying UI components such as banners and categories.
- **contact us**: Tests for the Contact Us form and its validation.

Each test is independent and performs specific actions on the website to validate the feature's functionality.

---

## TECHNOLOGIES USED

- **Python**: Programming language used for writing the tests.
- **Playwright**: A powerful browser automation tool that supports multiple browsers (Chromium, Firefox, WebKit).
- **Pytest**: A framework for running and organizing tests. It also handles test reporting.
- **Page Object Model (POM)**: Design pattern used for organizing and structuring tests.

---

## TEST CATEGORIES

The following are the major test categories that cover different areas of the Advantage Online Shopping website:

| Category      | Description                                      |
|---------------|--------------------------------------------------|
| **Cart**      | Validates adding/removing products to/from the cart. |
| **Checkout**  | Verifies the checkout process for logged-in and non-logged-in users. |
| **Login**     | Ensures that login functionality works correctly with valid, invalid, and empty credentials. |
| **Logout**    | Ensures that a user can log out successfully.     |
| **Registration** | Verifies user registration with valid and invalid details. |
| **Search**    | Tests the product search functionality with various inputs. |
| **UI**        | Validates clickable links, buttons, and other UI elements on the homepage. |
| **Contact Us** | Tests the "Contact Us" form submission and its response. |

---

## BEST PRACTICES

- **Isolation**: Each test is isolated and does not rely on others. Every test creates its own browser context and page.
- **Page Object Model**: Each page of the website is represented as a class in the `pages/` directory, encapsulating the actions a user can perform on that page.
- **Clear Naming**: Test files and functions are named clearly and descriptively to indicate the functionality being tested.
- **Use of Fixtures**: Shared fixtures (like the `page` fixture) are used to avoid repetitive code and ensure consistency across tests.

---

## CONTRIBUTION

Contributions are welcome! To contribute:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or bug fix.
4. Write your tests or code changes.
5. Create a pull request with a description of your changes.

Please ensure that new tests follow the POM structure and that existing tests are not broken.

---

## LICENSE

This project is licensed under the MIT License. You are free to use, modify, and distribute the code for personal or educational purposes.

