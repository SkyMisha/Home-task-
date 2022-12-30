import time

import pytest

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_message()
    page.should_be_price_in_basket_message()
    page.product_name_check()
    page.product_price_check()


@pytest.mark.parametrize('links', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
                                   "promo=offer5", "promo=offer6",
                                   pytest.param("promo=offer7", marks=pytest.mark.xfail),
                                   "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket2(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{links}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_message()
    page.should_be_price_in_basket_message()
    page.product_name_check()
    page.product_price_check()


@pytest.mark.xfail(reason="")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_is_not_present_after_adding_product()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.message_is_not_present_in_case_we_dont_add_the_product_to_the_basket()


@pytest.mark.xfail(reason="")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page. message_disappeared_adding_product()


















