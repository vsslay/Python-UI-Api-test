from pages.base_page import BasePage


class PracticeFormTab(BasePage):

    URL = "https://demoqa.com/automation-practice-form"

    FIRST_NAME_INPUT_LOCATOR = "//input[@id='firstName']"
    LAST_NAME_INPUT_LOCATOR = "//input[@id='lastName']"
    EMAIL_INPUT_LOCATOR = "//input[@id='userEmail']"
    PHONE_NUMBER_INPUT_LOCATOR = "//input[@id='userNumber']"
    GENDER_BUTTON_LOCATOR = "//label[contains(text(),'Male')]"
    SUBMIT_BUTTON_LOCATOR = "//button[@type='submit']"
    ADDRESS_INPUT_LOCATOR = "//*[@id='currentAddress']"

    BIRTH_DATE_SELECT_BUTTON_LOCATOR = "//input[@id='dateOfBirthInput']"
    YEAR_SELECT_BUTTON_LOCATOR = "//select[@class='react-datepicker__year-select']"
    PROPER_YEAR_BUTTON_LOCATOR = "//option[@value='1999']"
    MONTH_SELECT_LOCATOR = "//select[@class='react-datepicker__month-select']"
    PROPER_MONTH_BUTTON_LOCATOR = "//option[@value='4']"
    DATE_SELECT_BUTTON_LOCATOR = "//div[@class='react-datepicker__day react-datepicker__day--018']"
    SUBJECTS_INPUT_LOCATOR = "//*[@id='subjectsInput']"

    MUSIC_HOBBY_LOCATOR = "//*[contains(text(),'Music')]"
    READING_HOBBY_LOCATOR = "//*[contains(text(),'Reading')]"

    CHOOSE_STATE_LOCATOR = "//*[@id='react-select-3-input']"
    CHOOSE_CITY_LOCATOR = "//*[@id='react-select-4-input']"
    UPLOAD_PICTURE_LOCATOR = "//input[@id='uploadPicture']"
    CONFIRMATION_FORM_LOCATOR = "//div[@class='modal-body']"

    EXAMPLE_FILE_PATH = "C:\\Users\\ymaka\\Desktop\\Pro\\files_for_tests\\avatar.jpg"

    def navigate(self):
        self.url_open(self.URL)

    def input_date(self):
        self.click(self.BIRTH_DATE_SELECT_BUTTON_LOCATOR)
        self.click(self.YEAR_SELECT_BUTTON_LOCATOR)
        self.click(self.PROPER_YEAR_BUTTON_LOCATOR)
        self.click(self.MONTH_SELECT_LOCATOR)
        self.click(self.PROPER_MONTH_BUTTON_LOCATOR)
        self.click(self.DATE_SELECT_BUTTON_LOCATOR)

    def click_gender_and_hobbies(self):
        self.js_click(self.GENDER_BUTTON_LOCATOR)
        self.js_click(self.MUSIC_HOBBY_LOCATOR)
        self.js_click(self.READING_HOBBY_LOCATOR)

    def upload_avatar(self):
        self.upload_file(self.UPLOAD_PICTURE_LOCATOR, self.EXAMPLE_FILE_PATH)

    def input_subject_state_and_city(self):
        self.js_click(self.SUBJECTS_INPUT_LOCATOR)
        self.send_text(self.SUBJECTS_INPUT_LOCATOR, 'Comp')
        self.press_tab(self.SUBJECTS_INPUT_LOCATOR)
        self.js_click(self.CHOOSE_STATE_LOCATOR)
        self.send_text(self.CHOOSE_STATE_LOCATOR, 'Uttar')
        self.press_tab(self.CHOOSE_STATE_LOCATOR)
        self.js_click(self.CHOOSE_CITY_LOCATOR)
        self.send_text(self.CHOOSE_CITY_LOCATOR, 'Agra')
        self.press_tab(self.CHOOSE_CITY_LOCATOR)

    def input_user_information(self):
        self.send_text(self.FIRST_NAME_INPUT_LOCATOR, 'Sample')
        self.send_text(self.LAST_NAME_INPUT_LOCATOR, 'User')
        self.send_text(self.EMAIL_INPUT_LOCATOR, 'mail@example.com')
        self.send_text(self.PHONE_NUMBER_INPUT_LOCATOR, '9999887766')
        self.send_text(self.ADDRESS_INPUT_LOCATOR, 'Tbilisi, Georgia, Ana Politkovskaya str.')
        self.click_gender_and_hobbies()
        self.input_date()
        self.upload_file(self.UPLOAD_PICTURE_LOCATOR, self.EXAMPLE_FILE_PATH)
        self.input_subject_state_and_city()

    def click_submit_button(self):
        self.js_click(self.SUBMIT_BUTTON_LOCATOR)

    def check_confirmation_page_presence(self):
        self.wait_for_element_presence(self.CONFIRMATION_FORM_LOCATOR)

    def input_information_and_check_confirmation(self):
        try:
            self.input_user_information()
            self.click_submit_button()
            self.check_confirmation_page_presence()
            return True
        except Exception:
            return False