from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
        return True

    def should_be_added_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Message is not present"
        print("Message is present")

    def should_be_price_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRISE_IN_BASKET_MESSAGE), "Message is not present"
        print("message is present")

    def find_product_title(self) -> WebElement:
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return title

    def find_product_added_title(self):
        added_title = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TITLE)
        return added_title

    def find_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE)
        return product_price

    def find_current_price_in_basket(self):
        current_pice_in_bask = self.browser.find_element(*ProductPageLocators.CURRENT_PRISE_IN_BASKET)
        return current_pice_in_bask

    def product_name_check(self):
        title = self.find_product_title().text
        added_title = self.find_product_added_title().text
        assert title == added_title
        print(" Title Ok")

    def product_price_check(self):
        prise = self.find_product_price().text
        current_price = self.find_current_price_in_basket().text
        assert prise == current_price
        print("Price ok")

    def message_is_not_present_after_adding_product(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE),\
            "Message is present but shouldn't be"

    def message_is_not_present_in_case_we_dont_add_the_product_to_the_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE),\
            "Message is present but shouldn't be"

    def message_disappeared_adding_product(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE),\
            "The message is not disappeared but should"
