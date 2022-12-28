from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver.common.by import By


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()


# def test_guest_is_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = LoginPage(browser, link)
#     page.open()
#     assert page.is_login_url()


# def test_guest_should_be_login_url(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#
#
# def test_should_be_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_form()
#
#
# def test_should_be_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = LoginPage(browser, link)
#     main_page = MainPage(browser, link)
#     page.open()
#     page.should_be_register_form()


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
