import pytest
from selenium import webdriver


@pytest.yield_fixture()
def setUP():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one time setUp")
    if browser == 'chrome':
        baseURL = "https://the-internet.herokuapp.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on chrome")
    else:
        baseURL = "https://the-internet.herokuapp.com/"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        print("Running tests on FF")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
