import pytest
from selenium import webdriver


@pytest.fixture
def driver() -> webdriver.Chrome:
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        yield driver
