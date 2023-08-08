import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    driver.get("https://phptravels.net/admin")
    driver.implicitly_wait(5)
    return driver


#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     else:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.ChromeOptions(options=chrome_options)
#     driver.implicitly_wait(10)
#     return driver

@pytest.fixture(params=[
    ("admin@phptravels.com", "demoadmin", "Pass"),
    ("admin@phptravels.com1", "demoadmin", "Fail"),
    ("admin@phptravels.com", "demoadmin1", "Fail"),
    ("admin@phptravels.com1", "demoadmin1", "Fail")
])
def getDataforlogin(request):
    return request.param
