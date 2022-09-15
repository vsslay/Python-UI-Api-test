from pages.base_page import BasePage


class LinksTab(BasePage):

    URL = "https://demoqa.com/links"

    HOME_LINK = "//*[@id='simpleLink']"
    HOME_SEUR_LINK = "//*[@id='dynamicLink']"
    CREATED_LINK = "//*[@id='created']"
    NO_CONTENT_LINK = "//*[@id='no-content']"
    MOVED_LINK = "//*[@id='moved']"
    BAD_REQUEST_LINK = "//*[@id='bad-request']"
    UNAUTHORIZED_LINK = "//*[@id='unauthorized']"
    FORBIDDEN_LINK = "//*[@id='forbidden']"
    NOT_FOUND_LINK = "//*[@id='dynamicLink']"

    RESPONSE_CODE_LOCATOR = "//*[@id='linkResponse']"

    def navigate(self):
        self.url_open(self.URL)

    def click_link_and_check_response(self, locator, expected_code):
        self.js_click(locator)
        response = self.get_element_text(self.RESPONSE_CODE_LOCATOR)
        if str(expected_code) in response:
            pass
        else:
            return f"expected {expected_code} code, got {response}"

    def click_and_check_broken_links(self):
        self.click_link_and_check_response(self.CREATED_LINK, 201)
        self.click_link_and_check_response(self.NO_CONTENT_LINK, 204)
        self.click_link_and_check_response(self.MOVED_LINK, 301)
        self.click_link_and_check_response(self.BAD_REQUEST_LINK, 400)
        self.click_link_and_check_response(self.UNAUTHORIZED_LINK, 401)
        self.click_link_and_check_response(self.FORBIDDEN_LINK, 403)
        self.click_link_and_check_response(self.NOT_FOUND_LINK, 404)

    def click_and_check_working_links(self):
        self.click(self.HOME_LINK)
        self.click(self.HOME_SEUR_LINK)
        self.switch_window(1)
        self.close_window()
        self.switch_window(1)
        self.close_window()

    def click_and_check_links(self):
        try:
            self.click_and_check_broken_links()
            self.click_and_check_working_links()
            return True
        except Exception:
            return False

