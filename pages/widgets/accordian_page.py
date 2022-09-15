from pages.base_page import BasePage


class AccordianTab(BasePage):
    URL = "https://demoqa.com/accordian"

    FIRST_CONTENT_HEADING_LOCATOR = "//*[@id='section1Heading']"
    SECOND_CONTENT_HEADING_LOCATOR = "//*[@id='section2Heading']"
    THIRD_CONTENT_HEADING_LOCATOR = "//*[@id='section3Heading']"

    FIRST_CONTENT_LOCATOR = "//*[@id='section1Content']"
    SECOND_CONTENT_LOCATOR = "//*[@id='section2Content']"
    THIRD_CONTENT_LOCATOR = "//*[@id='section3Content']"

    def navigate(self):
        self.url_open(self.URL)

    def check_text_is_visible(self, locator, text):
        element_text = self.get_element_text(locator)
        expected_text = text
        if expected_text in element_text:
            pass
        else:
            quit("No expected text in element text")

    def check_all_tubs(self):
        try:
            self.check_text_is_visible(self.FIRST_CONTENT_LOCATOR, "Lorem Ipsum is simply dummy text")
            self.left_click(self.FIRST_CONTENT_HEADING_LOCATOR)
            self.scroll_to_element(self.THIRD_CONTENT_HEADING_LOCATOR)
            self.left_click(self.SECOND_CONTENT_HEADING_LOCATOR)
            self.check_text_is_visible(self.SECOND_CONTENT_LOCATOR, "Lorem Ipsum is not simply random text")
            self.left_click(self.SECOND_CONTENT_HEADING_LOCATOR)
            self.scroll_to_element(self.THIRD_CONTENT_HEADING_LOCATOR)
            self.left_click(self.THIRD_CONTENT_HEADING_LOCATOR)
            self.scroll_to_element(self.THIRD_CONTENT_LOCATOR)
            self.check_text_is_visible(self.THIRD_CONTENT_LOCATOR, "The point of using Lorem Ipsum")
            return True
        except Exception:
            quit("Expected all buttons pressed and text appeared")
