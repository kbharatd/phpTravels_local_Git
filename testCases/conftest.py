import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    # driver.get("https://phptravels.net/admin")
    driver.implicitly_wait(5)
    return driver
