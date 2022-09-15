from pages.base_page import BasePage


class ResizableTab(BasePage):

    URL = "https://demoqa.com/resizable"

    RESIZE_IN_FRAME_LOCATOR = "//*[@id='resizableBoxWithRestriction']/span"
    RESIZE_ON_PAGE_LOCATOR = "//*[@id='resizable']/span"

    def navigate(self):
        self.url_open(self.URL)

    def resize_all_boxes(self):
        self.scroll_to_element(self.RESIZE_ON_PAGE_LOCATOR)
        self.drag_and_drop_by_coordinates(self.RESIZE_IN_FRAME_LOCATOR, 250, 50)
        self.drag_and_drop_by_coordinates(self.RESIZE_ON_PAGE_LOCATOR, 10, 10)
        return True