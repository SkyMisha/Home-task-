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

    # def chek_link_parametr(self):
