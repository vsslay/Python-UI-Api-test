from pages.base_page import BasePage


class DatePickerTab(BasePage):
    URL = "https://demoqa.com/date-picker"

    SELECT_DATE_LOCATOR = "//*[@id='datePickerMonthYearInput']"
    MONTH_SELECT_LOCATOR = "//select[@class='react-datepicker__month-select']"
    YEAR_SELECT_LOCATOR = "//select[@class='react-datepicker__year-select']"
    PROPER_YEAR_BUTTON_LOCATOR = "//option[@value='1999']"
    PROPER_MONTH_BUTTON_LOCATOR = "//option[@value='4']"
    DATE_SELECT_BUTTON_LOCATOR = "//div[@class='react-datepicker__day react-datepicker__day--018']"

    DATE_AND_TIME_PICKER_LOCATOR = "//*[@id='dateAndTimePickerInput']"
    NEXT_MONTH_BUTTON_LOCATOR = "//button[contains(text(), 'Next Month')]"
    YEAR_PICK_LOCATOR = "//*[@class='react-datepicker__year-read-view--selected-year']"
    PROPER_YEAR_LOCATOR = "//*[@id='dateAndTimePicker']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[6]"
    PROPER_DATE_SELECT_LOCATOR = "//div[contains(text(),'13')]"
    PROPER_TIME_SELECT_LOCATOR = "//li[contains(text(),'11:15')]"

    def navigate(self):
        self.url_open(self.URL)

    def input_date_selection(self):
        self.click(self.SELECT_DATE_LOCATOR)
        self.click(self.MONTH_SELECT_LOCATOR)
        self.click(self.PROPER_MONTH_BUTTON_LOCATOR)
        self.click(self.YEAR_SELECT_LOCATOR)
        self.click(self.PROPER_YEAR_BUTTON_LOCATOR)
        self.click(self.DATE_SELECT_BUTTON_LOCATOR)
        self.get_element_value(self.SELECT_DATE_LOCATOR)
        pass

    def input_date_and_time(self):
        self.click(self.DATE_AND_TIME_PICKER_LOCATOR)
        self.click(self.NEXT_MONTH_BUTTON_LOCATOR)
        self.click(self.YEAR_PICK_LOCATOR)
        self.click(self.PROPER_YEAR_LOCATOR)
        self.click(self.PROPER_DATE_SELECT_LOCATOR)
        self.click(self.PROPER_TIME_SELECT_LOCATOR)
        self.get_element_value(self.DATE_AND_TIME_PICKER_LOCATOR)
        pass

    def check_date_and_time_inputs(self):
        try:
            self.input_date_selection()
            self.input_date_and_time()
            return True
        except Exception:
            quit("Date is not valid")
