import pytest
from selenium import webdriver
from Webpages.pim_page import LoginPage
from Webpages.pim_page import PIMPage


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()  # Make sure to have the appropriate WebDriver installed and in PATH
    driver.get('https://opensource-demo.orangehrmlive.com')

    # Login
    login_page = LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()

    yield driver
    driver.quit()


def test_add_new_employee(setup):
    driver = setup
    pim_page = PIMPage(driver)

    # Navigate to PIM module
    pim_page.navigate_to_pim()

    # Add new employee
    pim_page.click_add_button()
    pim_page.enter_first_name("John")
    pim_page.enter_last_name("Doe")
    pim_page.click_save_button()

    # Assert success message
    expected_success_message = "Successfully Saved"  # Adjust the expected message based on the actual application
    assert expected_success_message in pim_page.get_success_message()


def test_edit_existing_employee(setup):
    driver = setup
    pim_page = PIMPage(driver)

    # Navigate to PIM module
    pim_page.navigate_to_pim()

    # Search for an existing employee
    pim_page.search_employee("John Doe")
    pim_page.select_employee()

    # Edit employee details
    pim_page.click_edit_button()
    pim_page.enter_first_name("Johnathan")
    pim_page.enter_last_name("Doe-Smith")
    pim_page.click_save_button()

    # Assert success message
    expected_success_message = "Successfully Saved"  # Adjust the expected message based on the actual application
    assert expected_success_message in pim_page.get_success_message()