from QAtools.pages.base_page import BasePage


class RadioButtonTab(BasePage):

    URL = "https://demoqa.com/radio-button"

    YES_BUTTON_LOCATOR = "//*[@id='yesRadio']"
    IMPRESSIVE_BUTTON_LOCATOR = "//*[@id='impressiveRadio']"
    NO_BUTTON_LOCATOR = "//*[@id='noRadio']"
    YES_DISPLAYED_LOCATOR = "//p[@class='mt-3']/*[contains(text(), 'Yes')]"
    IMPRESSIVE_DISPLAYED_LOCATOR = "//p[@class='mt-3']/*[contains(text(), 'Impressive')]"
    NO_DISPLAYED_LOCATOR = "//p[@class='mt-3']/*[contains(text(), 'No')]"

    def navigate(self):
        self.url_open(self.URL)

    def click_and_check_yes_button(self):
        self.js_click(self.YES_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.YES_DISPLAYED_LOCATOR)

    def click_and_check_impressive_button(self):
        self.js_click(self.IMPRESSIVE_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.IMPRESSIVE_DISPLAYED_LOCATOR)

    def click_and_check_no_button(self):
        self.js_click(self.NO_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.IMPRESSIVE_DISPLAYED_LOCATOR)

    def click_and_check_buttons(self):
        try:
            self.click_and_check_yes_button()
            self.click_and_check_impressive_button()
            self.click_and_check_no_button()
            return True
        except Exception:
            return False
