import allure

from data import Format, fake
from data.models import PersonData
from pages.base_page import BasePage
from locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    _URL = 'https://demoqa.com/text-box'

    _last_person_data: PersonData

    @allure.step('Generate new person data')
    def _generate_new_person_data(self) -> None:
        self._last_person_data = PersonData()

    @property
    @allure.step('Get name field text')
    def _name_field_text(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.FULL_NAME_TEXT_INPUT).get_attribute('value')

    @property
    @allure.step('Get email field text')
    def _email_field_text(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.EMAIL_TEXT_INPUT).get_attribute('value')

    @property
    @allure.step('Get current address field text')
    def _current_address_field_text(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.CURRENT_ADDRESS_TEXT_AREA).get_attribute('value')

    @property
    @allure.step('Get permanent address field text')
    def _permanent_address_field_text(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.PERMANENT_ADDRESS_TEXT_AREA).get_attribute('value')

    @_name_field_text.setter
    @allure.step('Set name field text')
    def _name_field_text(self, name: str) -> None:
        name_field = self._wait_element_visibility(TextBoxPageLocators.FULL_NAME_TEXT_INPUT)
        name_field.send_keys(name)

    @_email_field_text.setter
    @allure.step('Set email field text')
    def _email_field_text(self, email: str) -> None:
        email_field = self._wait_element_visibility(TextBoxPageLocators.EMAIL_TEXT_INPUT)
        email_field.send_keys(email)

    @_current_address_field_text.setter
    @allure.step('Set current address field text')
    def _current_address_field_text(self, current_address: str) -> None:
        current_address_field = self._wait_element_visibility(TextBoxPageLocators.CURRENT_ADDRESS_TEXT_AREA)
        current_address_field.send_keys(current_address)

    @_permanent_address_field_text.setter
    @allure.step('Set permanent address field text')
    def _permanent_address_field_text(self, permanent_address: str) -> None:
        permanent_address_field = self._wait_element_visibility(TextBoxPageLocators.PERMANENT_ADDRESS_TEXT_AREA)
        permanent_address_field.send_keys(permanent_address)

    @property
    @allure.step('Get output name')
    def _output_name(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.NAME_OUTPUT).text.split(':')[1]

    @property
    @allure.step('Get output email')
    def _output_email(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.EMAIL_OUTPUT).text.split(':')[1]

    @property
    @allure.step('Get output current address')
    def _output_current_address(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.CURRENT_ADDRESS_OUTPUT).text.split(':')[1]

    @property
    @allure.step('Get output permanent address')
    def _output_permanent_address(self) -> str:
        return self._wait_element_visibility(TextBoxPageLocators.PERMANENT_ADDRESS_OUTPUT).text.split(':')[1]

    @allure.step('Fill all fields')
    def fill_all_fields(self) -> None:
        self._generate_new_person_data()

        self._name_field_text = self._last_person_data.name
        self._email_field_text = self._last_person_data.email
        self._current_address_field_text = self._last_person_data.current_address
        self._permanent_address_field_text = self._last_person_data.permanent_address

    @allure.step('Fill all fields with extra spaces')
    def fill_all_fields_with_extra_spaces(self) -> None:
        self._generate_new_person_data()

        self._name_field_text = Format.add_extra_spaces(self._last_person_data.name)
        self._email_field_text = Format.add_extra_spaces(self._last_person_data.email)
        self._current_address_field_text = Format.add_extra_spaces(self._last_person_data.current_address)
        self._permanent_address_field_text = Format.add_extra_spaces(self._last_person_data.permanent_address)

    @allure.step('Fill email field with invalid format data')
    def fill_email_field_with_invalid_format_data(self) -> None:
        self._email_field_text = fake.text(20)

    @allure.step('Click submit button')
    def click_submit_button(self) -> None:
        self._wait_element_visibility(TextBoxPageLocators.SUBMIT_BUTTON).click()

    @allure.step('Check fields are empty')
    def must_empty_fields(self) -> None:
        assert self._name_field_text == '', \
            'name field is not empty'
        assert self._name_field_text == '', \
            'email field is not empty'
        assert self._name_field_text == '', \
            'current address field is not empty'
        assert self._name_field_text == '', \
            'permanent address field is not empty'

    @allure.step('Check output block is empty')
    def must_empty_output(self) -> None:
        assert self._wait_element_presence(TextBoxPageLocators.OUTPUT_BLOCK).text == ''

    @allure.step('Check fields are right filled')
    def must_right_filled_fields(self) -> None:
        assert self._name_field_text == self._last_person_data.name, \
            'name in field is not same with filled'
        assert self._email_field_text == self._last_person_data.email, \
            'email in field is not same with filled'
        assert self._current_address_field_text == self._last_person_data.current_address, \
            'current address in field is not same with filled'
        assert self._permanent_address_field_text == self._last_person_data.permanent_address, \
            'permanent address in field is not same with filled'

    @allure.step('Check for right output')
    def must_right_output(self) -> None:
        assert self._output_name == self._last_person_data.name, \
            'output name is not same with filled'
        assert self._output_email == self._last_person_data.email, \
            'output email is not same with filled'
        assert self._output_current_address == self._last_person_data.current_address.replace('\n', ' '), \
            'output current address is not same with filled'
        assert (self._output_permanent_address ==
                self._last_person_data.permanent_address.replace('\n', ' ')), \
            'output permanent address is not same with filled'
