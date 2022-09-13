from QAtools.pages.base_page import BasePage


class SelectableTab(BasePage):

    URL = "https://demoqa.com/selectable"

    LIST_SELECT_LOCATOR = "//li[contains(text(),"
    GRID_SELECT_LOCATOR = "//*[@id='gridContainer']/*/li[contains(text(),"

    SWITCH_TO_GRID_LOCATOR = "//a[contains(text(),'Grid')]"

    def navigate(self):
        self.url_open(self.URL)

    def choose_all_options(self):
        self.scroll_down()
        self.click(self.LIST_SELECT_LOCATOR + "'Cras justo odio')]")
        self.click(self.LIST_SELECT_LOCATOR + "'Dapibus ac facilisis in')]")
        self.click(self.LIST_SELECT_LOCATOR + "'Morbi leo risus')]")
        self.click(self.LIST_SELECT_LOCATOR + "'Porta ac consectetur ac')]")
        self.click(self.SWITCH_TO_GRID_LOCATOR)
        self.click(self.GRID_SELECT_LOCATOR + "'One')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Two')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Three')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Four')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Five')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Six')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Seven')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Eight')]")
        self.click(self.GRID_SELECT_LOCATOR + "'Nine')]")
        return True
