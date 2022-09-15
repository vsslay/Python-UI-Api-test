from pages.base_page import BasePage


class ButtonsTab(BasePage):

    URL = "https://demoqa.com/buttons"

    DOUBLE_CLICK_BUTTON_LOCATOR = "//button[contains(text(),'Double')]"
    RIGHT_CLICK_BUTTON_LOCATOR = "//button[contains(text(),'Right')]"
    DYNAMIC_CLICK_BUTTON_LOCATOR = "//html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button"
    DOUBLE_CLICK_DISPLAYED_LOCATOR = "//p[contains(text(),'double click')]"
    RIGHT_CLICK_DISPLAYED_LOCATOR = "//p[contains(text(),'right click')]"
    DYNAMIC_CLICK_DISPLAYED_LOCATOR = "//p[contains(text(),'dynamic click')]"

    def navigate(self):
        self.url_open(self.URL)

    def double_click_and_check_button(self):
        self.double_click(self.DOUBLE_CLICK_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.DOUBLE_CLICK_DISPLAYED_LOCATOR)

    def right_click_and_check_button(self):
        self.right_click(self.RIGHT_CLICK_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.RIGHT_CLICK_DISPLAYED_LOCATOR)

    def dynamic_click_and_check_button(self):
        self.click(self.DYNAMIC_CLICK_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.DYNAMIC_CLICK_DISPLAYED_LOCATOR)

    def click_and_check_buttons(self):
        try:
            self.double_click_and_check_button()
            self.right_click_and_check_button()
            self.dynamic_click_and_check_button()
            return True
        except Exception:
            return False
