import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_button(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg").text
    assert button == "Ajouter au panier"
    time.sleep(5)
