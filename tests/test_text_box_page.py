import allure
import pytest

from pages import TextBoxPage


@allure.feature('Text box page')
class TestTextBoxPage:
    @allure.title('Right URL')
    def test_right_url(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.must_right_url()

    @allure.title('Fields is empty after loading page')
    def test_fields_is_empty_after_loading_page(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.must_empty_fields()

    @allure.title('Output is empty after loading page')
    def test_output_block_is_empty_after_loading_page(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.must_empty_output()

    @allure.title('Fields can be filled')
    def test_fields_can_be_filled(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.fill_all_fields()
        page.must_right_filled_fields()

    @allure.title('Output is right')
    def test_output_is_right(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.fill_all_fields()
        page.click_submit_button()
        page.must_right_output()

    @allure.title('Extra spaces cut off in output')
    @pytest.mark.xfail(reason='Extra spaces in name are not cut off')
    def test_extra_spaces_cut_off_in_output(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.fill_all_fields_with_extra_spaces()
        page.click_submit_button()
        page.must_right_output()

    @allure.title('Invalid email data does not pass')
    def test_invalid_format_email_data_does_not_pass(self, driver):
        page = TextBoxPage(driver)
        page.open()
        page.fill_email_field_with_invalid_format_data()
        page.click_submit_button()
        page.must_empty_output()
