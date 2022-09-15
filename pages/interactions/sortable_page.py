from pages.base_page import BasePage


class SortableTab(BasePage):

    URL = "https://demoqa.com/sortable"

    LIST_DRAG_LOCATOR = "//*[@id='demo-tabpane-list']/div/div[3]"
    GRID_DRAG_LOCATOR = "//*[@id='demo-tabpane-grid']/div/div/div[3]"

    SWITCH_TO_GRID_LOCATOR = "//a[contains(text(),'Grid')]"

    def navigate(self):
        self.url_open(self.URL)

    def drag_all_options(self):
        self.drag_and_drop_by_coordinates(self.LIST_DRAG_LOCATOR, 0, 50)
        listed_numbers = self.get_element_text("//*[@id='demo-tabpane-list']/div")
        if listed_numbers == 'One\nTwo\nFour\nThree\nFive\nSix':
            self.click(self.SWITCH_TO_GRID_LOCATOR)
            self.drag_and_drop_by_coordinates(self.GRID_DRAG_LOCATOR, -50, -100)
            grid_numbers = list[self.get_element_text("//*[@id='demo-tabpane-grid']")]
            if grid_numbers == 'Three\nOne\nTwo\nFour\nFive\nSix\nSeven\nEight\nNine':
                pass
        return True