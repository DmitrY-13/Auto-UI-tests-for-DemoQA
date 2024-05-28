from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME_TEXT_INPUT = By.CSS_SELECTOR, 'input#userName'
    EMAIL_TEXT_INPUT = By.CSS_SELECTOR, 'input#userEmail'
    CURRENT_ADDRESS_TEXT_AREA = By.CSS_SELECTOR, 'textarea#currentAddress'
    PERMANENT_ADDRESS_TEXT_AREA = By.CSS_SELECTOR, 'textarea#permanentAddress'

    SUBMIT_BUTTON = By.CSS_SELECTOR, 'button#submit'

    OUTPUT_BLOCK = By.CSS_SELECTOR, 'div#output'

    NAME_OUTPUT = By.CSS_SELECTOR, 'p#name'
    EMAIL_OUTPUT = By.CSS_SELECTOR, 'p#email'
    CURRENT_ADDRESS_OUTPUT = By.CSS_SELECTOR, 'p#currentAddress'
    PERMANENT_ADDRESS_OUTPUT = By.CSS_SELECTOR, 'p#permanentAddress'
