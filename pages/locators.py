from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main >h1 ")
    PRODUCT_PRISE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_ADDED_TITLE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRISE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner >p")
    CURRENT_PRISE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner >p >strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn")


class BasketItems:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner >p ")
