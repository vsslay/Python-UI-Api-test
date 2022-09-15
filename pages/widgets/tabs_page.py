from pages.base_page import BasePage


class TabsPageTab(BasePage):
    URL = "https://demoqa.com/tabs"

    FIRST_CONTENT_HEADING_LOCATOR = "//*[@id='demo-tab-what']"
    SECOND_CONTENT_HEADING_LOCATOR = "//*[@id='demo-tab-origin']"
    THIRD_CONTENT_HEADING_LOCATOR = "//*[@id='demo-tab-use']"

    FIRST_CONTENT_LOCATOR = "//*[@id='demo-tabpane-what']/p[1]/text()"
    SECOND_CONTENT_LOCATOR = "//*[@id='demo-origin-what']/p[1]/text()"
    THIRD_CONTENT_LOCATOR = "//*[@id='demo-use-what']/p[1]/text()"

    def navigate(self):
        self.url_open(self.URL)

    def check_all_tubs(self):
        try:
            self.left_click(self.SECOND_CONTENT_HEADING_LOCATOR)
            self.left_click(self.THIRD_CONTENT_HEADING_LOCATOR)
            self.left_click(self.FIRST_CONTENT_HEADING_LOCATOR)
            return True
        except Exception:
            quit("Expected all buttons pressed and text appeared")
