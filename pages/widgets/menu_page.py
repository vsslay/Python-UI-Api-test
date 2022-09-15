from pages.base_page import BasePage


class MenuTab(BasePage):
    URL = "https://demoqa.com/menu"

    MAIN_ITEM_ONE_LOCATOR = "//ul[@id='nav']/li[1]"
    MAIN_ITEM_TWO_LOCATOR = "//ul[@id='nav']/li[2]"
    MAIN_ITEM_THREE_LOCATOR = "//ul[@id='nav']/li[3]"
    SUB_ITEM_ONE_LOCATOR = "//ul[@id='nav']/li[2]/ul/li[1]"
    SUB_ITEM_TWO_LOCATOR = "//ul[@id='nav']/li[2]/ul/li[2]"
    SUB_SUB_ITEM_LIST_LOCATOR = "//ul[@id='nav']/li[2]/ul/li[3]"
    SUB_SUB_ITEM_ONE_LOCATOR = "//ul[@id='nav']/li[2]/ul/li[3]/ul/li[1]"
    SUB_SUB_ITEM_TWO_LOCATOR = "//ul[@id='nav']/li[2]/ul/li[3]/ul/li[2]"

    def navigate(self):
        self.url_open(self.URL)

    def click_all_items(self):
        self.js_click(self.MAIN_ITEM_ONE_LOCATOR)
        self.js_click(self.MAIN_ITEM_THREE_LOCATOR)
        self.js_click(self.MAIN_ITEM_TWO_LOCATOR)
        self.js_click(self.SUB_ITEM_ONE_LOCATOR)
        self.js_click(self.SUB_ITEM_TWO_LOCATOR)
        self.js_click(self.SUB_SUB_ITEM_LIST_LOCATOR)
        self.js_click(self.SUB_SUB_ITEM_ONE_LOCATOR)
        self.js_click(self.SUB_SUB_ITEM_TWO_LOCATOR)
        return True
