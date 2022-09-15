from pages.base_page import BasePage


class BrokenLinkTab(BasePage):

    URL = "https://demoqa.com/broken"

    WORKING_IMAGE_LOCATOR = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[1]"
    BROKEN_IMAGE_LOCATOR = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[2]"
    WORKING_LINK_LOCATOR = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[1]"
    BROKEN_LINK_URL = "http://the-internet.herokuapp.com/status_codes/500"

    def navigate(self):
        self.url_open(self.URL)

    def check_links(self):
        try:
            self.wait_for_element_presence(self.BROKEN_IMAGE_LOCATOR)
            self.wait_for_element_presence(self.WORKING_IMAGE_LOCATOR)
            self.js_click(self.WORKING_LINK_LOCATOR)
            self.get_back()
            self.check_response_code(self.BROKEN_LINK_URL, 500)
            return True
        except Exception:
            return False
