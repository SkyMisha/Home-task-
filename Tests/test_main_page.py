from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_is_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    assert page.is_login_url()


def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    main_page = MainPage(browser, link)
    page.open()
    page.should_be_register_form()


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()
#
#
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    basket_page = page.go_to_basket()
    basket_page.product_is_not_present()
    basket_page.basket_is_empty()
