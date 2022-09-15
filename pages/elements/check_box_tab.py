from pages.base_page import BasePage


class CheckBoxTab(BasePage):

    URL = "https://demoqa.com/checkbox"

    EXTEND_BUTTON_LOCATOR = "//*[@id='tree-node']/div/button[1]"
    CHECKBOXES_LOCATOR = "//*[@id='tree-node']//span[@class='rct-checkbox']"
    ACTIVE_ELEMENT_LOCATOR = "//*[@class='text-success']"

    def navigate(self):
        self.url_open(self.URL)

    def click_extend_button(self):
        self.click(self.EXTEND_BUTTON_LOCATOR)

    def click_checkboxes(self):
        self.click(self.CHECKBOXES_LOCATOR)

    def click_on_checkboxes(self):
        self.navigate()
        self.click_extend_button()
        self.click_checkboxes()

    def count_active_elements(self):
        list_of_checkboxes = []
        index = 1
        while index < 18:
            text_of_element = self.get_element_text(self.ACTIVE_ELEMENT_LOCATOR + f"[{index}]")
            list_of_checkboxes.append(text_of_element)
            index = index + 1
        return len(list_of_checkboxes)
