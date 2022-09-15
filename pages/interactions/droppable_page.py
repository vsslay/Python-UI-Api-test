from pages.base_page import BasePage


class DroppableTab(BasePage):

    URL = "https://demoqa.com/droppable"

    SIMPLE_DRAGABBLE_LOCATOR = "//*[@id='draggable']"
    DRAGABBLE_ACCEPTABLE_LOCATOR = "//div[@id='acceptable']"
    DRAGABBLE_NOT_ACCEPTABLE_LOCATOR = "//div[@id='notAcceptable']"
    PROPOGATION_DRAGABBLE_LOCATOR = "//*[@id='dragBox']"
    REVERT_DRAGABBLE_LOCATOR = "//*[@id='revertable']"
    NOT_REVERT_DRAGABBLE_LOCATOR = "//*[@id='notRevertable']"

    ACCEPT_TAB_LOCATOR = "//a[contains(text(),'Accept')]"
    PROPOGATION_TAB_LOCATOR = "//a[contains(text(),'Prevent')]"
    REVERT_TAB_LOCATOR = "//a[contains(text(),'Revert')]"

    SIMPLE_BOX_TO_DROP_LOCATOR = "//div[2]/div[2]/div/div[1]/div/div[2]"
    ACCEPT_BOX_TO_DROP_LOCATOR = "//div[2]/div[2]/div/div[2]/div/div[2]"
    REVERT_BOX_TO_DROP_LOCATOR = "//div[2]/div[2]/div/div[4]/div/div[2]"
    OUTER_BOX_LOCATOR = "//*[@id='notGreedyDropBox']"
    INNER_BOX_LOCATOR = " //*[@id='notGreedyInnerDropBox']"
    GREEDY_OUTER_BOX_LOCATOR = "//*[@id='greedyDropBox']"
    GREEDY_OUTER_BOX_TEXT_LOCATOR = "//*[@id='greedyDropBox']/p"
    GREEDY_INNER_BOX_LOCATOR = " //*[@id='greedyDropBoxInner']"

    BOX_IS_DROPPED_LOCATOR = "/*[contains(text(),'Dropped!')]"

    def navigate(self):
        self.url_open(self.URL)

    def check_dropbox_activated(self, locator):
        box_is_activated = locator + "/*[contains(text(),'Dropped!')]"
        self.wait_for_element_presence(box_is_activated)

    def drag_all_droppable_properties(self):
        self.wait_for_element_presence(self.SIMPLE_BOX_TO_DROP_LOCATOR)
        self.wait_for_element_presence(self.SIMPLE_DRAGABBLE_LOCATOR)
        self.drag_and_drop_object_to_object(self.SIMPLE_DRAGABBLE_LOCATOR, self.SIMPLE_BOX_TO_DROP_LOCATOR)
        self.drag_and_drop_by_coordinates(self.SIMPLE_DRAGABBLE_LOCATOR, 1, 1)
        self.check_dropbox_activated(self.SIMPLE_BOX_TO_DROP_LOCATOR)
        self.click(self.ACCEPT_TAB_LOCATOR)
        self.drag_and_drop_object_to_object(self.DRAGABBLE_NOT_ACCEPTABLE_LOCATOR, self.ACCEPT_BOX_TO_DROP_LOCATOR)
        self.drag_and_drop_object_to_object(self.DRAGABBLE_ACCEPTABLE_LOCATOR, self.ACCEPT_BOX_TO_DROP_LOCATOR)
        self.check_dropbox_activated(self.ACCEPT_BOX_TO_DROP_LOCATOR)
        self.click(self.PROPOGATION_TAB_LOCATOR)
        self.drag_and_drop_object_to_object(self.PROPOGATION_DRAGABBLE_LOCATOR, self.OUTER_BOX_LOCATOR)
        self.drag_and_drop_object_to_object(self.PROPOGATION_DRAGABBLE_LOCATOR, self.INNER_BOX_LOCATOR)
        self.drag_and_drop_object_to_object(self.PROPOGATION_DRAGABBLE_LOCATOR, self.GREEDY_INNER_BOX_LOCATOR)
        self.drag_and_drop_object_to_object(self.PROPOGATION_DRAGABBLE_LOCATOR, self.GREEDY_OUTER_BOX_TEXT_LOCATOR)
        self.drag_and_drop_object_to_object(self.PROPOGATION_DRAGABBLE_LOCATOR, self.GREEDY_INNER_BOX_LOCATOR)
        self.check_dropbox_activated(self.OUTER_BOX_LOCATOR)
        self.check_dropbox_activated(self.INNER_BOX_LOCATOR)
        self.click(self.REVERT_TAB_LOCATOR)
        self.drag_and_drop_object_to_object(self.REVERT_DRAGABBLE_LOCATOR, self.REVERT_BOX_TO_DROP_LOCATOR)
        self.drag_and_drop_object_to_object(self.NOT_REVERT_DRAGABBLE_LOCATOR, self.REVERT_BOX_TO_DROP_LOCATOR)
        self.check_dropbox_activated(self.REVERT_BOX_TO_DROP_LOCATOR)
        return True
