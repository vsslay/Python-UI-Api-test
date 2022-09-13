from QAtools.pages.base_page import BasePage


class SelectMenuTab(BasePage):
    URL = "https://demoqa.com/select-menu"

    SELECT_VALUE_LOCATOR = "//input[@id='react-select-2-input']"
    SELECT_ONE_LOCATOR = "//input[@id='react-select-3-input']"
    SELECT_MENU_LOCATOR = "//*[@id='oldSelectMenu']"
    SELECT_DROPDOWN_LOCATOR = "//input[@id='react-select-4-input']"

    SELECT_PROPER_MENU_LOCATOR = "//*[contains(text(),'Black')]"
    SELECT_MULTIPLE_LOCATOR = "//option[contains(text(),"

    VALUE_CONTAINER_LOCATOR = "//*[@id='withOptGroup']/div/div[1]"
    SELECT_ONE_CONTAINER_LOCATOR = "//*[@id='selectOne']/div/div[1]"
    DROPDOWN_CONTAINER_LOCATOR = "//*[@id='selectMenuContainer']/div[7]/div/div/div/div[1]"

    def navigate(self):
        self.url_open(self.URL)

    def choose_right_options_from_menus(self):
        self.send_text(self.SELECT_VALUE_LOCATOR, "A Root")
        self.press_tab(self.SELECT_VALUE_LOCATOR)
        self.send_text(self.SELECT_ONE_LOCATOR, "Mr")
        self.press_tab(self.SELECT_ONE_LOCATOR)
        self.click(self.SELECT_MENU_LOCATOR)
        self.click(self.SELECT_PROPER_MENU_LOCATOR)
        self.scroll_to_element(self.SELECT_DROPDOWN_LOCATOR)
        self.send_text(self.SELECT_DROPDOWN_LOCATOR, "Gree")
        self.press_tab(self.SELECT_DROPDOWN_LOCATOR)
        self.send_text(self.SELECT_DROPDOWN_LOCATOR, "Blu")
        self.press_tab(self.SELECT_DROPDOWN_LOCATOR)
        self.send_text(self.SELECT_DROPDOWN_LOCATOR, "Re")
        self.press_tab(self.SELECT_DROPDOWN_LOCATOR)
        self.hold_ctrl()
        self.click(self.SELECT_MULTIPLE_LOCATOR + "'Volvo')]")
        self.click(self.SELECT_MULTIPLE_LOCATOR + "'Saab')]")
        self.click(self.SELECT_MULTIPLE_LOCATOR + "'Opel')]")
        self.click(self.SELECT_MULTIPLE_LOCATOR + "'Audi')]")
        self.stop_hold_ctrl()
        pass

    def check_properties_text(self):
        value_box_expected_text = "A root option"
        select_one_box_expected_text = "Mr."
        value_box_text = self.get_element_text(self.VALUE_CONTAINER_LOCATOR)
        select_one_box_text = self.get_element_text(self.SELECT_ONE_CONTAINER_LOCATOR)
        dropdown_box_text = self.get_element_text(self.DROPDOWN_CONTAINER_LOCATOR)
        if value_box_expected_text in value_box_text and "Green" in dropdown_box_text and "Blue" in dropdown_box_text\
                and "Red" in dropdown_box_text and select_one_box_expected_text in select_one_box_text:
            pass
        else:
            quit("Wrong text in boxes detected")

    def check_select_menus(self):
        self.choose_right_options_from_menus()
        self.check_properties_text()
        return True
