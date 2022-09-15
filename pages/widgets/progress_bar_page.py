from pages.base_page import BasePage


class ProgressBarTab(BasePage):
    URL = "https://demoqa.com/progress-bar"

    START_STOP_BUTTON_LOCATOR = "//button[@id='startStopButton']"
    PROGRESS_BAR_BEFORE_START_LOCATOR = "//div[@aria-valuenow='0']"
    PROGRESS_BAR_SUCCESS_LOCATOR = "//div[@aria-valuenow='0']"
    RESET_BUTTON_LOCATOR = "//button[@id='resetButton']"

    def navigate(self):
        self.url_open(self.URL)

    def check_progress_bar(self):
        self.wait_for_element_presence(self.PROGRESS_BAR_BEFORE_START_LOCATOR)
        self.click(self.START_STOP_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.PROGRESS_BAR_SUCCESS_LOCATOR)
        self.wait_for_element_presence(self.RESET_BUTTON_LOCATOR)
        self.click(self.RESET_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.PROGRESS_BAR_BEFORE_START_LOCATOR)
        return True
