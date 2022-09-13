from QAtools.pages.base_page import BasePage


class NestedIframePage(BasePage):

    URL = "https://demoqa.com/nestedframes"

    PARENT_IFRAME_LOCATOR = "//iframe[@src='/sampleiframe']"
    CHILD_IFRAME_LOCATOR = "//iframe[@srcdoc='<p>Child Iframe</p>']"

    def navigate(self):
        self.url_open(self.URL)

    def switch_between_nested_iframes(self):
        try:
            self.switch_to_iframe(self.PARENT_IFRAME_LOCATOR)
            self.switch_to_iframe(self.CHILD_IFRAME_LOCATOR)
            self.switch_to_default_frame()
            return True
        except Exception:
            return False