from selenium import webdriver
from selenium.webdriver.common.by import By
from base.driver_service import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

    link_login = "//a[contains(text(),'Form Authentication')]"
    userNameXpath = "//input[@id='username']"
    passwordXpath = "//input[@id='password']"
    logInBTNXpath = "//button[@class='radius']"
    textXpath = "//h4[@class='subheader']"

    def click_login_link(self):
        self.element_click(self.link_login, locator_type="xpath")

    def enter_user(self, username):
        self.send_keys(username, self.userNameXpath, locator_type="xpath")

    def enter_password(self, password):
        self.send_keys(password, self.passwordXpath, locator_type="xpath")

    def click_login_btn(self):
        self.element_click(self.logInBTNXpath, locator_type="xpath")

    def introduce_text(self, text_in_element):
        self.get_text(text_in_element, self.textXpath, locator_type="xpath")

    def login(self, username="", password=""):
        self.click_login_link()
        self.enter_user(username)
        self.enter_password(password)
        self.click_login_btn()

    def verify_login_successful_text(self, text_to_verify=""):
        self.introduce_text(text_to_verify)

    def verify_login_failed(self):
        result = self.is_element_present("flash error", locator_type="classname")
        return result
