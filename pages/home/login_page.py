from selenium import webdriver
from selenium.webdriver.common.by import By
from base.driver_service import SeleniumDriver
import time


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    link_login = "//a[contains(text(),'Form Authentication')]"
    userNameXpath = "//input[@id='username']"
    passwordXpath = "//input[@id='password']"
    logInBTNXpath = "//button[@class='radius']"

    def click_login_link(self):
        self.element_click(self.link_login, locator_type="xpath")

    def enter_user(self, username):
        self.send_keys(username, self.userNameXpath)

    def enter_password(self, password):
        self.send_keys(password, self.passwordXpath)

    def click_login_btn(self):
        self.element_click(self.logInBTNXpath, locator_type="xpath")

    def login(self, username="", password=""):
        self.click_login_link()
        self.enter_user(username)
        self.enter_password(password)
        self.click_login_btn()
        time.sleep(2)

    def verify_login_successful(self):
        result = self.is_element_present("flash success",
                                         locator_type="class")
        return result

    def verify_login_failed(self):
        result = self.is_element_present("flash error",
                                         locator_type="class")
        return result
