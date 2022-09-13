import pytest
import allure


class TestAlertFrameWindowPage:

    @allure.description("This test clicks links and checks if all new windows are opened")
    @pytest.mark.usefixtures("setup_for_browser_windows")
    def test_browser_windows_tab(self, browser_windows):
        browser_windows_check = browser_windows.check_all_tabs_and_windows()
        assert browser_windows_check, "Expected all pages opened and urls are proper, got no opened urls instead"

    @allure.description("This test clicks on modal dialog links and checks if all modal dialogs are opened properly")
    @pytest.mark.usefixtures("setup_for_modal_dialogs")
    def test_modal_dialogs_tab(self, modal_dialogs):
        modal_dialogs_check = modal_dialogs.check_all_tabs_and_windows()
        assert modal_dialogs_check, "Expected all modal dialogs opened and urls are proper, " \
                                    "got wrong parameters of modal windows instead instead"

    @allure.description("This test calls alerts of different types and solves them")
    @pytest.mark.usefixtures("setup_for_alerts_tab")
    def test_alerts_tab(self, alerts_page_tab):
        check_alerts_tab = alerts_page_tab.check_all_alerts()
        assert check_alerts_tab, "Expected all alerts confirmed, got no alert confirmation instead"

    @allure.description("This test switches between iframes")
    @pytest.mark.usefixtures("setup_for_iframe_tab")
    def test_iframe_tab(self, iframe_tab):
        check_iframe_page = iframe_tab.switch_between_iframes()
        assert check_iframe_page, "Expected user can switch between iframes, got no switch between frames instead"

    @allure.description("This test switches between child and parent iframes")
    @pytest.mark.usefixtures("setup_for_nested_iframe_tab")
    def test_nested_iframe_tab(self, nested_iframe_tab):
        check_nested_iframe_page = nested_iframe_tab.switch_between_nested_iframes()
        assert check_nested_iframe_page, "Expected user can switch between child and parent iframes, " \
                                         "got no switch between frames instead"
