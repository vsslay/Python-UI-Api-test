from QAtools.pages.base_page import BasePage


class WebTablesTab(BasePage):

    URL = "https://demoqa.com/webtables"

    ADD_BUTTON_LOCATOR = "//button[@id='addNewRecordButton']"
    FIRST_NAME_INPUT_LOCATOR = "//input[@id='firstName']"
    LAST_NAME_INPUT_LOCATOR = "//input[@id='lastName']"
    EMAIL_INPUT_LOCATOR = "//input[@id='userEmail']"
    AGE_INPUT_LOCATOR = "//input[@id='age']"
    SALARY_INPUT_LOCATOR = "//input[@id='salary']"
    DEPARTMENT_INPUT_LOCATOR = "//input[@id='department']"
    SUBMIT_BUTTON_LOCATOR = "//button[@id='submit']"
    SEARCH_BAR_LOCATOR = "//input[@id='searchBox']"

    NEW_USER_PRESENCE_LOCATOR = "//*[contains(text(),'mail@example.com')]"

    def navigate(self):
        self.url_open(self.URL)

    def click_add_button(self):
        self.js_click(self.ADD_BUTTON_LOCATOR)

    def input_user_information(self):
        self.send_text(self.FIRST_NAME_INPUT_LOCATOR, 'Sample')
        self.send_text(self.LAST_NAME_INPUT_LOCATOR, 'User')
        self.send_text(self.EMAIL_INPUT_LOCATOR, 'mail@example.com')
        self.send_text(self.AGE_INPUT_LOCATOR, '25')
        self.send_text(self.SALARY_INPUT_LOCATOR, '1000')
        self.send_text(self.DEPARTMENT_INPUT_LOCATOR, 'QA Team')

    def click_submit_button(self):
        self.js_click(self.SUBMIT_BUTTON_LOCATOR)

    def click_and_input_name_to_search(self):
        self.js_click(self.SEARCH_BAR_LOCATOR)
        self.send_text(self.SEARCH_BAR_LOCATOR, 'Sample')

    def check_new_user_presence(self):
        self.wait_for_element_presence(self.NEW_USER_PRESENCE_LOCATOR)

    def input_information_and_check_new_user_created(self):
        try:
            self.click_add_button()
            self.input_user_information()
            self.click_submit_button()
            self.click_and_input_name_to_search()
            self.check_new_user_presence()
            return True
        except Exception:
            return False
