from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from selenium import webdriver
import logging


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locator_type)
            print("Element Found")
        except NameError:
            print("Element Not Found")
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except NoSuchElementException:
            print("Element not found")
            return False

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except ElementNotInteractableException:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def get_text(self, elem_text,  locator, locator_type="id"):
        try:
            elem_text_list = []
            element = self.get_element(locator, locator_type)
            text_contains = element.get_attribute('innerHTML')

            for i in text_contains:
                elem_text_list.append(i)

            elem_text_str = ''.join(map(str, elem_text_list))

            if elem_text == elem_text_str:
                print(elem_text)
                self.log.info("get_text: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                print(elem_text_list)
                self.log.info("No get_text type: " + locator +
                              " locatorType: " + locator_type + "text is:" + elem_text_list)
                return False
        except ElementNotInteractableException:
            self.log.info("No get_text type: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except ElementNotInteractableException:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()
