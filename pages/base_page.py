from typing import Final

import allure
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import Locator

DEFAULT_TIMEOUT: Final[float] = 5


class BasePage:
    _URL: str

    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver

    @allure.step('Open page')
    def open(self):
        self._driver.get(self._URL)

    def _wait_element_visibility(self, locator: Locator, timeout: float = DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            ec.visibility_of_element_located(locator),
            'Element is not visible'
        )

    def _wait_element_presence(self, locator: Locator, timeout: float = DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(
            ec.presence_of_element_located(locator),
            'Element is not presence'
        )

    @allure.step('Check for right url')
    def must_right_url(self):
        assert self._driver.current_url == self._URL, 'Wrong URL'
