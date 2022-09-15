from pages.base_page import BasePage


class SliderTab(BasePage):
    URL = "https://demoqa.com/slider"

    SLIDER_LOCATOR = "//input[@type='range']"
    SLIDER_RANGE_LOCATOR = "//*[@id='sliderValue']"

    def navigate(self):
        self.url_open(self.URL)

    def slide_and_check_slider(self):
        self.send_value(self.SLIDER_RANGE_LOCATOR, "0")
        value = self.get_element_value(self.SLIDER_RANGE_LOCATOR)
        while value != "100":
            self.send_value(self.SLIDER_RANGE_LOCATOR, int(value) + 1)
            value = self.get_element_value(self.SLIDER_RANGE_LOCATOR)
        return True

