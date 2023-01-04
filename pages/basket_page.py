from pages.base_page import BasePage
from pages.locators import BasketItems, BasePageLocators


class BasketPage(BasePage):
    def product_is_not_present(self):
        assert self.is_not_element_present(*BasketItems.BASKET_ITEMS)

    def basket_is_empty(self):
        assert self.is_element_present(*BasketItems.EMPTY_BASKET_MESSAGE)

