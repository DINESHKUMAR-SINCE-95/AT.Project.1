import pytest
from selenium import webdriver
from Webpage.login_page import LoginPage


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()  # Make sure to have the appropriate WebDriver installed and in PATH
    driver.get('http://your-orangehrm-url.com')
    yield driver
    driver.quit()

def test_successful_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Test data
    username = "Admin"
    password = "admin123"

    # Perform login
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # Assert user is logged in successfully
    assert "dashboard" in driver.current_url  # Adjust this assertion based on actual post-login URL or elements

def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    # Test data
    username = "Admin"
    password = "Invalid password"

    # Perform login
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # Assert error message for invalid credentials
    expected_error_message = "Invalid credentials"
    assert login_page.get_error_message() == expected_error_message