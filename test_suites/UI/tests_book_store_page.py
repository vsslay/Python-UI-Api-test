import pytest
import allure


class TestBookStorePage:

    @allure.description("This test makes full cycle of creating new user, making new order of goods and delete account")
    @pytest.mark.usefixtures("setup_for_book_store_page")
    def test_book_store_page(self, login_and_register_tab, profile_tab, book_store_tab):
        bookstore_tab_check = login_and_register_tab.is_opened()
        assert bookstore_tab_check, "Expected after all manipulations passed, account deleted" \
                                    " - login page to be opened, got no confirmation of page is opened instead"
