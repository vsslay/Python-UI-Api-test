from pages.base_page import BasePage


class BookStorePage(BasePage):

    BOOK_GIT_POCKET_GUIDE_LOCATOR = "//a[contains(text(),'Git Pocket Guide')]"
    BOOK_SPEAKING_JAVA_LOCATOR = "//a[contains(text(),'Speaking JavaScript')]"
    BOOK_DESIGNING_API_LOCATOR = "//a[contains(text(),'Designing Evolvable Web APIs with ASP.NET')]"

    ADD_BOOK_TO_COLLECTION_BUTTON_LOCATOR = "//button[contains(text(),'Add To Your Collection')]"
    BACK_TO_STORE_BUTTON_LOCATOR = "//button[contains(text(),'Back To Book Store')]"
    GO_TO_PROFILE_BUTTON = "//span[contains(text(),'Profile')]"

    BOOK_STORE_IS_OPENED_LOCATOR = "//div[@class='pattern-backgound playgound-header']"

    def add_new_book_to_collection(self):
        self.scroll_down()
        self.wait_for_element_presence(self.ADD_BOOK_TO_COLLECTION_BUTTON_LOCATOR)
        self.click(self.ADD_BOOK_TO_COLLECTION_BUTTON_LOCATOR)
        self.wait_for_alert_presence()
        self.accept_alert()
        self.scroll_down()
        self.wait_for_element_presence(self.BACK_TO_STORE_BUTTON_LOCATOR)
        self.click(self.BACK_TO_STORE_BUTTON_LOCATOR)
        self.wait_for_element_presence(self.BOOK_STORE_IS_OPENED_LOCATOR)
        self.scroll_down()

    def add_books_to_collection(self):
        self.click(self.BOOK_GIT_POCKET_GUIDE_LOCATOR)
        self.add_new_book_to_collection()
        self.click(self.BOOK_SPEAKING_JAVA_LOCATOR)
        self.add_new_book_to_collection()
        self.click(self.BOOK_DESIGNING_API_LOCATOR)
        self.add_new_book_to_collection()
        self.click(self.GO_TO_PROFILE_BUTTON)
