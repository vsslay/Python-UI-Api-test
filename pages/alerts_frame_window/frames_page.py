from QAtools.pages.base_page import BasePage


class IframePage(BasePage):

    URL = "https://demoqa.com/frames"

    LARGE_IFRAME_LOCATOR = "//*[@id='frame1']"
    SMALL_IFRAME_LOCATOR = "//*[@id='frame2']"

    def navigate(self):
        self.url_open(self.URL)

    def switch_between_iframes(self):
        try:
            self.switch_to_iframe(self.LARGE_IFRAME_LOCATOR)
            self.switch_to_default_frame()
            self.switch_to_iframe(self.SMALL_IFRAME_LOCATOR)
            return True
        except Exception:
            return False
