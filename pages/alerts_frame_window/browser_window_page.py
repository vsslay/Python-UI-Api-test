from pages.base_page import BasePage


class BrowserWindowTab(BasePage):
    URL = "https://demoqa.com/browser-windows"

    NEW_TAB_BUTTON_LOCATOR = "//*[@id='tabButton']"
    NEW_WINDOW_BUTTON_LOCATOR = "//*[@id='windowButton']"
    NEW_WINDOW_MESSAGE_BUTTON_LOCATOR = "//*[@id='messageWindowButton']"

    NEW_TAB_URL = "https://demoqa.com/sample"

    def navigate(self):
        self.url_open(self.URL)

    def check_all_tabs_and_windows(self):
        try:
            self.click(self.NEW_TAB_BUTTON_LOCATOR)
            self.switch_window(1)
            self.close_window()
            self.switch_window(0)
            self.click(self.NEW_WINDOW_BUTTON_LOCATOR)
            self.switch_window(1)
            self.close_window()
            self.switch_window(0)
            self.click(self.NEW_WINDOW_MESSAGE_BUTTON_LOCATOR)
            self.switch_window(1)
            self.close_window()
            return True
        except Exception:
            return False


