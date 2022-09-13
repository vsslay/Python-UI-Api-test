from QAtools.pages.base_page import BasePage


class ModalDialogsTab(BasePage):
    URL = "https://demoqa.com/modal-dialogs"

    SMALL_MODAL_BUTTON_LOCATOR = "//*[@id='showSmallModal']"
    LARGE_MODAL_BUTTON_LOCATOR = "//*[@id='showLargeModal']"
    CLOSE_SMALL_MODAL_BUTTON_LOCATOR = "//*[@id='closeSmallModal']"
    CLOSE_LARGE_MODAL_BUTTON_LOCATOR = "//*[@id='closeLargeModal']"
    MODAL_CONTENT_WINDOW_LOCATOR = "//html/body/div[4]/div/div"

    def navigate(self):
        self.url_open(self.URL)

    def check_modal_size(self, height, width):
        self.wait_for_element_presence(self.MODAL_CONTENT_WINDOW_LOCATOR)
        size_of_element = self.get_element_size(self.MODAL_CONTENT_WINDOW_LOCATOR)
        expected_size = {'height': height, 'width': width}
        if size_of_element == expected_size:
            pass
        else:
            quit('Size is not valid')

    def open_check_and_close_small_modal(self):
        self.click(self.SMALL_MODAL_BUTTON_LOCATOR)
        self.check_modal_size(222, 300)
        self.click(self.CLOSE_SMALL_MODAL_BUTTON_LOCATOR)

    def open_check_and_close_large_modal(self):
        self.click(self.LARGE_MODAL_BUTTON_LOCATOR)
        self.check_modal_size(430, 500)
        self.click(self.CLOSE_LARGE_MODAL_BUTTON_LOCATOR)

    def check_all_tabs_and_windows(self):
        try:
            self.open_check_and_close_small_modal()
            self.open_check_and_close_large_modal()
            return True
        except Exception:
            return str(Exception)
