import pytest
import selenium
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help='Choose from langs: (en/ru/ua/...)')
    parser.addoption("--browser", action='store', default='chrome')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption('browser')
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    yield browser
    time.sleep(5)
    browser.quit()
