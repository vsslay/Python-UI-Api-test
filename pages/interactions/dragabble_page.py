from QAtools.pages.base_page import BasePage


class DragabbleTab(BasePage):

    URL = "https://demoqa.com/dragabble"

    SIMPLE_DRAGABBLE_LOCATOR = "//div[contains(text(),'Drag me')]"

    AXIS_TAB_LOCATOR = "//a[contains(text(),'Axis')]"
    AXIS_DRAGABBLE_X_LOCATOR = "//div[contains(text(),'Only X')]"
    AXIS_DRAGABBLE_Y_LOCATOR = "//div[contains(text(),'Only Y')]"

    CONTAINER_TAB_LOCATOR = "//a[contains(text(),'Container')]"
    CONTAINER_BOX_DRAGABBLE_LOCATOR = "//div[@class = 'draggable ui-widget-content ui-draggable ui-draggable-handle']"
    CONTAINER_FRAME_DRAGABBLE_LOCATOR = " //span[contains(text(),'contained within my parent')]"

    CURSOR_TAB_LOCATOR = "//a[contains(text(),'Cursor')]"
    CURSOR_CENTER_LOCATOR = "//div[contains(text(),'center')]"
    CURSOR_LEFT_LOCATOR = "//div[contains(text(),'left')]"
    CURSOR_BOTTOM_LOCATOR = "//div[@id='cursorBottom']"

    def navigate(self):
        self.url_open(self.URL)

    def drag_all_properties(self):
        self.scroll_down()
        self.drag_and_drop_by_coordinates(self.SIMPLE_DRAGABBLE_LOCATOR, 150, 175)
        self.click(self. AXIS_TAB_LOCATOR)
        self.drag_and_drop_by_coordinates(self.AXIS_DRAGABBLE_X_LOCATOR, 100, 0)
        self.drag_and_drop_by_coordinates(self.AXIS_DRAGABBLE_Y_LOCATOR, 0, 100)
        self.click(self.CONTAINER_TAB_LOCATOR)
        self.drag_and_drop_by_coordinates(self.CONTAINER_BOX_DRAGABBLE_LOCATOR, 25, -20)
        self.drag_and_drop_by_coordinates(self.CONTAINER_FRAME_DRAGABBLE_LOCATOR, 5, -10)
        self.click(self.CURSOR_TAB_LOCATOR)
        self.drag_and_drop_by_coordinates(self.CURSOR_CENTER_LOCATOR, 150, 175)
        self.drag_and_drop_by_coordinates(self.CURSOR_LEFT_LOCATOR, 150, 175)
        self.drag_and_drop_by_coordinates(self.CURSOR_BOTTOM_LOCATOR, 15, 15)
        return True
