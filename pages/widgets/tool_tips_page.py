from pages.base_page import BasePage


class ToolTipsTab(BasePage):
    URL = "https://demoqa.com/tool-tips"

    HOVER_BUTTON_LOCATOR = "//button[@id='toolTipButton']"
    HOVER_FIELD__LOCATOR = "//*[@id='toolTipTextField']"
    HOVER_HYPERLINK_LOCATOR = "//*[@id='texToolTopContainer']/a[1]"
    HOVER_HYPERLINK_SECOND_LOCATOR = "//*[@id='texToolTopContainer']/a[2]"

    HOVER_PRESENCE_LOCATOR = "//*[contains(text(),'You hovered over')]"

    def navigate(self):
        self.url_open(self.URL)

    def check_hoovers_are_visible(self):
        self.hover_mouse(self.HOVER_BUTTON_LOCATOR)
        self.hover_mouse(self.HOVER_FIELD__LOCATOR)
        self.hover_mouse(self.HOVER_HYPERLINK_LOCATOR)
        self.hover_mouse(self.HOVER_HYPERLINK_SECOND_LOCATOR)
        return True
