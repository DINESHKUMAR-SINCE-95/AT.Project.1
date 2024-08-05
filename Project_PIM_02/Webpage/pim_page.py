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


class PIM02:
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

    def submitBtn(self):
        self.driver.find_element(by=By.TAG_NAME, value='button').click()
        self.sleep(10)

    def quit(self):
        self.driver.quit()

    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def login(self, data1, data2, data3, data4, data5, data6):
        try:
            self.boot()
            self.inputBox('username', self.username)
            self.inputBox('password', self.password)
            self.submitBtn()
            self.sleep(3)

            # login in webpage
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
            self.sleep(5)

            # go to PIM left pane to the webpage
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
            self.sleep(5)
            self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i').click()
            self.sleep(3)

            #tab use for skip the boxes
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()


            firstNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input')
            firstNameElement.send_keys(data1)
            self.sleep(5)
            self.action.send_keys(Keys.TAB).perform()


            secondNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input')
            secondNameElement.send_keys(data2)
            self.sleep(2)
            self.action.send_keys(Keys.TAB).perform()


            thirdNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input')
            thirdNameElement.send_keys(data3)
            self.sleep(2)

            # four name element is used for fill the details
            fourNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input')
            fourNameElement.send_keys(data4)
            self.sleep(2)


            fiveNameElement = self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
            fiveNameElement.send_keys(data5)
            self.sleep(2)


            sixNameElement = self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
            sixNameElement.send_keys(data6)
            self.sleep(5)

            self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
            self.sleep(10)

            print('The exiting employee is successfully edited')
        except NoSuchElementException:
            print('no new employee is added')


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
obj = PIM02(url,'Admin','admin123')
obj.login('01','02','03','04','05','06')