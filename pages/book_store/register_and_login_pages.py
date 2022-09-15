from pages.base_page import BasePage
import requests


class RegisterLoginPage(BasePage):

    URL = "https://demoqa.com/login"

    USER_NAME_INPUT_LOCATOR = "//input[@placeholder='UserName']"
    PASSWORD_INPUT_LOCATOR = "//input[@placeholder='Password']"

    LOGIN_BUTTON_LOCATOR = "//button[@id='login']"
    REGISTRATION_BUTTON_LOCATOR = "//button[@id='newUser']"

    REGISTER_FIRST_NAME_INPUT_LOCATOR = "//input[@id='firstname']"
    REGISTER_LAST_NAME_INPUT_LOCATOR = "//input[@id='lastname']"
    REGISTER_USERNAME_INPUT_LOCATOR = "//input[@id='userName']"
    REGISTER_PASSWORD_INPUT_LOCATOR = "//input[@id='password']"
    CAPTCHA_LOCATOR = "//*[@id='recaptcha-anchor']/div[1]"

    REGISTER_BUTTON_LOCATOR = "//button[@id='register']"
    BACK_TO_LOGIN_BUTTON_LOCATOR = "//button[@id='gotologin']"

    CREDENTIALS_USERNAME = "vsslay"
    CREDENTIALS_PASSWORD = "Password_12345!"

    LOGIN_PAGE_HEADER_LOCATOR = "//div[contains(text(),'Login')]"

    def navigate(self):
        self.url_open(self.URL)

    def create_new_user(self):
        self.click(self.REGISTRATION_BUTTON_LOCATOR)
        self.send_text(self.REGISTER_FIRST_NAME_INPUT_LOCATOR, "Andrew")
        self.send_text(self.REGISTER_LAST_NAME_INPUT_LOCATOR, "Khrystsiuk")
        self.send_text(self.REGISTER_USERNAME_INPUT_LOCATOR, self.CREDENTIALS_USERNAME)
        self.send_text(self.REGISTER_PASSWORD_INPUT_LOCATOR, self.CREDENTIALS_PASSWORD)
        self.scroll_down()
        self.click(self.BACK_TO_LOGIN_BUTTON_LOCATOR)

    def create_new_user_request(self):
        url_to_create_user = "https://demoqa.com/Account/v1/User"
        data_to_create_user = {
            "userName": "vsslay",
            "password": "Password_12345!"
        }
        requests.post(url_to_create_user, data_to_create_user)

    def login_to_account(self):
        self.send_text(self.USER_NAME_INPUT_LOCATOR, self.CREDENTIALS_USERNAME)
        self.send_text(self.PASSWORD_INPUT_LOCATOR, self.CREDENTIALS_PASSWORD)
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def create_user_and_login_to_account(self):
        self.create_new_user()
        self.create_new_user_request()
        self.login_to_account()

    def is_opened(self):
        self.wait_for_element_presence(self.LOGIN_PAGE_HEADER_LOCATOR)
        return True
