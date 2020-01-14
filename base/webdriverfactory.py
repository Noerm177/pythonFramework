"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser
        """
                Set chrome driver and iexplorer environment based on OS

                chromedriver = "C:/.../chromedriver.exe"
                os.environ["webdriver.chrome.driver"] = chromedriver
                self.driver = webdriver.Chrome(chromedriver)

                PREFERRED: Set the path on the machine where browser will be executed
            """

    def get_web_driver_instance(self):
        """
               Get WebDriver Instance based on the browser configuration

                Returns:
                    'WebDriver Instance'
                """
        baseURL = "https://the-internet.herokuapp.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
            # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(6)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
