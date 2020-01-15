import pytest
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setUP():
    print("Running method level setUp")
    yield
    print("\nRunning method level tearDown")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operation system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")
