from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def is_login_url(self):
        return True if 'login' in self.url else False

    def should_be_login_url(self):
        assert "login" in self.url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "fail"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "fail"

    def register_new_user(self, email, password):
        element_email = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        element_email.send_keys(email)
        element_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        element_password.send_keys(password)
        element_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        element_confirm_password.send_keys(password)
        element_confirm_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        element_confirm_button.click()


