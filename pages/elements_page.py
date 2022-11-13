import time

from locators.elements_pages_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators
    def fill_field_and_submit(self):
        self.element_is_visible(self.locators.FULL_NAME).send.keys('INFOTECH')
        self.element_is_visible(self.locators.EMAIL).send.keys('test@com.ua')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send.keys('test_adress')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send.keys('test_two_adress')
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)

        # self.element_is_visible(self.locators.)
        # self.element_is_visible(self.locators.)
        # self.element_is_visible(self.locators.)


