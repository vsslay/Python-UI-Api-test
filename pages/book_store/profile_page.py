from QAtools.pages.base_page import BasePage


class ProfilePage(BasePage):

    GO_TO_BOOKSTORE_LOCATOR = "//div[@class='text-left button']/button[@id='gotoStore']"
    DELETE_ALL_BOOKS_BUTTON_LOCATOR = "//div[@class='text-right button di']/button[contains(text(),'Delete All Books')]"
    CONFIRM_DELETE_BUTTON_LOCATOR = "//button[@id='closeSmallModal-ok']"
    DELETE_ACCOUNT_BUTTON_LOCATOR = "//div[@class='text-center button']/button[contains(text(),'Delete Account')]"
    BOOK_TO_DELETE_LOCATOR = "//*[@id='delete-record-undefined']"
    ROW_CHANGE_LOCATOR = "//select"
    PROPER_ROW_LOCATOR = "//option[@value='10']"
    BOOK_NAME_INPUT_LOCATOR = "//input[@id='searchBox']"

    def go_to_bookstore(self):
        self.wait_for_element_presence(self.GO_TO_BOOKSTORE_LOCATOR)
        self.scroll_down()
        self.click(self.GO_TO_BOOKSTORE_LOCATOR)

    def confirm_delete(self):
        self.wait_for_element_presence(self.CONFIRM_DELETE_BUTTON_LOCATOR)
        self.js_click(self.CONFIRM_DELETE_BUTTON_LOCATOR)
        self.wait_for_alert_presence()
        self.accept_alert()

    def delete_all_books(self):
        self.scroll_down()
        self.click(self.DELETE_ALL_BOOKS_BUTTON_LOCATOR)
        self.confirm_delete()

    def delete_account(self):
        self.scroll_down()
        self.click(self.DELETE_ACCOUNT_BUTTON_LOCATOR)
        self.confirm_delete()

    def change_rows(self):
        self.scroll_down()
        self.click(self.ROW_CHANGE_LOCATOR)
        self.click(self.PROPER_ROW_LOCATOR)

    def find_and_delete_book(self):
        self.send_text(self.BOOK_NAME_INPUT_LOCATOR, "Designing")
        self.click(self.BOOK_TO_DELETE_LOCATOR)
        self.confirm_delete()
        self.clear_element_text(self.BOOK_NAME_INPUT_LOCATOR)
        self.scroll_down()

    def manipulate_books_in_profile(self):
        self.change_rows()
        self.find_and_delete_book()
        self.delete_all_books()
        self.delete_account()
