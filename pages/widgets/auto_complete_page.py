from pages.base_page import BasePage


class AutoCompleteTab(BasePage):
    URL = "https://demoqa.com/auto-complete"

    MULTIPLE_COLOR_INPUT_LOCATOR = "//input[@id='autoCompleteMultipleInput']"
    SINGLE_COLOR_INPUT_LOCATOR = "//input[@id='autoCompleteSingleInput']"

    FIRST_OF_MULTIPLE_COLORS_LOCATOR = "//*[@id='autoCompleteMultipleContainer']/div/div[1]/div[1]"
    SECOND_OF_MULTIPLE_COLORS_LOCATOR = "//*[@id='autoCompleteMultipleContainer']/div/div[1]/div[2]"
    SINGLE_COLOR_LOCATOR = "//*[@id='autoCompleteSingleContainer']/div/div[1]/div[1]"

    def navigate(self):
        self.url_open(self.URL)

    def input_colors(self):
        self.send_text(self.MULTIPLE_COLOR_INPUT_LOCATOR, "Bla")
        self.press_tab(self.MULTIPLE_COLOR_INPUT_LOCATOR)
        self.send_text(self.MULTIPLE_COLOR_INPUT_LOCATOR, 'Gree')
        self.press_tab(self.MULTIPLE_COLOR_INPUT_LOCATOR)
        self.send_text(self.SINGLE_COLOR_INPUT_LOCATOR, 'Whi')
        self.press_tab(self.SINGLE_COLOR_INPUT_LOCATOR)

    def check_input_colors(self):
        first_color = self.get_element_text(self.FIRST_OF_MULTIPLE_COLORS_LOCATOR)

        if first_color == "Black":
            second_color = self.get_element_text(self.SECOND_OF_MULTIPLE_COLORS_LOCATOR)
            if second_color == "Green":
                single_color = self.get_element_text(self.SINGLE_COLOR_LOCATOR)
                if single_color == "White":
                    pass
                else:
                    quit("Single color is other than expected")
            else:
                quit("Second color is other than expected")
        else:
            quit("First color is other than expected")

    def check_all_colors_are_as_expected(self):
        self.input_colors()
        self.check_input_colors()
        return True
