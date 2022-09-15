from pages.base_page import BasePage


class DynamicProperties(BasePage):

    URL = "https://demoqa.com/dynamic-properties"

    DYNAMIC_TEXT_LOCATOR = "//html/body/div[2]/div/div/div[2]/div[2]/div[2]/p"
    ENABLE_DELAY_BUTTON_LOCATOR = "//*[@id='enableAfter']"
    COLOR_CHANGE_BUTTON_LOCATOR = "//*[@id='colorChange']"
    VISIBILITY_DELAY_LOCATOR = "//*[@id='visibleAfter']"

    def navigate(self):
        self.url_open(self.URL)

    def check_dynamic_text(self):
        element_text = self.get_element_text(self.DYNAMIC_TEXT_LOCATOR)
        expected_text = "This text has random Id"
        if expected_text in element_text:
            pass
        else:
            quit(f"Expected text was '{expected_text}', got '{element_text}' instead")

    def check_button_is_active(self):
        self.check_if_element_active(self.ENABLE_DELAY_BUTTON_LOCATOR)

    def check_button_color(self):
        element_color = self.get_element_attribute(self.COLOR_CHANGE_BUTTON_LOCATOR, "color")
        expected_color = "rgba(220, 53, 69, 1)"
        if expected_color in element_color:
            pass
        else:
            quit(f"Expected {expected_color}, got {element_color}")

    def check_button_is_visible(self):
        self.wait_for_element_presence(self.VISIBILITY_DELAY_LOCATOR)

    def check_dynamic_properties(self):
        try:
            self.check_dynamic_text()
            self.check_button_is_visible()
            self.check_button_color()
            self.check_button_is_active()
            return True
        except Exception:
            return False

