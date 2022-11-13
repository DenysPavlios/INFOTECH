import pytest

from pages.form_page import FormPage
import time


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com')
        form_page.open()
        time.sleep(3)
