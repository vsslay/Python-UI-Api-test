from pages.base_page import BasePage


class TextBoxTab(BasePage):

    URL = "https://demoqa.com/text-box"

    USERNAME_INPUT_LOCATOR = "//input[@id='userName']"
    EMAIL_INPUT_LOCATOR = "//input[@id='userEmail']"
    SUBMIT_BUTTON_LOCATOR = "//button[@id='submit']"
    CURRENT_ADDRESS_INPUT_LOCATOR = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS_INPUT_LOCATOR = "//textarea[@id='permanentAddress']"
    CONFIRMATION_FIELD_LOCATOR = "//div[@class='border col-md-12 col-sm-12']"

    def navigate(self):
        self.url_open(self.URL)

    def input_user_name(self, name_text):
        self.send_text(self.USERNAME_INPUT_LOCATOR, name_text)

    def input_user_email(self, email_text):
        self.send_text(self.EMAIL_INPUT_LOCATOR, email_text)

    def input_current_address(self, current_address_text):
        self.send_text(self.CURRENT_ADDRESS_INPUT_LOCATOR, current_address_text)

    def input_permanent_address(self, permanent_address_text):
        self.send_text(self.PERMANENT_ADDRESS_INPUT_LOCATOR, permanent_address_text)

    def click_submit_button(self):
        self.js_click(self.SUBMIT_BUTTON_LOCATOR)

    def wait_for_confirmation(self):
        try:
            self._find_element(self.CONFIRMATION_FIELD_LOCATOR)
            return True
        except TimeoutError:
            return False

    def input_information_to_form(self):
        self.input_user_name('Andrew')
        self.input_user_email('mail@example.com')
        self.input_current_address('Tbilisi, Georgia, Ana Politkovskaya street 5, building 15')
        self.input_permanent_address('Minsk, Belarus, Kalinovskogo str. 52')
        self.click_submit_button()
