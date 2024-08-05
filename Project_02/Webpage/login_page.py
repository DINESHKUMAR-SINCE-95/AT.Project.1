from Data import data
from Locator import locator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


class LoginAutomation:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self, second):
        sleep(second)

    def inputBox(self, value, keys):
        self.driver.find_element(by=By.NAME, value=value).send_keys(keys)
        self.sleep(5)

    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def submitBtn(self):
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
        self.sleep(10)

    def quit(self):
        self.driver.quit()

    def login(self, data):
        try:
            self.boot()
            self.inputBox('username', self.username)
            self.inputBox('password', self.password)
            self.submitBtn()
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input').click()
            self.sleep(10)
            firstNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
            firstNameElement.send_keys(data)
            self.sleep(10)
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
            self.sleep(10)

            print('Reset password link send successfully')
        except NoSuchElementException:
            print('A valid error message for invalid credentials is displayed')


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
obj = LoginAutomation(url, 'Admin', 'admin123')
obj.login('Dinesh')
