from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver.Chrome, url: str):
        self._driver = driver
        self._url = url

    def open(self):
        self._driver.get(self._url)
