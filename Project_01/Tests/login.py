import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Webpage.Loginpage import LoginPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.load()
        login_page.enter_username('Admin')
        login_page.enter_password('admin123')
        login_page.submit()

        assert dashboard_page.verify_login() == True, "Login failed, dashboard not found!"