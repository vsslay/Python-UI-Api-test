import pytest
import allure


class TestWidgetsPage:

    @allure.description("This test presses tabs and checks if proper text appears")
    @pytest.mark.usefixtures("setup_for_accordian_tab")
    def test_accordian_tab(self, accordian_tab):
        accordian_tab_check = accordian_tab.check_all_tubs()
        assert accordian_tab_check, "Expected all buttons pressed and text appears, got no text appeared instead"

    @allure.description("This test sends part of the needed string and checks if autocomplete gave the rest of string")
    @pytest.mark.usefixtures("setup_for_auto_complete_tab")
    def test_auto_complete_tab(self, auto_complete_tab):
        auto_complete_tab_check = auto_complete_tab.check_all_colors_are_as_expected()
        assert auto_complete_tab_check, "Expected all colors presented, got no expected color instead"

    @allure.description("This test chooses date from widget and checks if date is proper")
    @pytest.mark.usefixtures("setup_for_date_picker_tab")
    def test_date_picker_tab(self, date_picker_tab):
        check_date_picker_tab = date_picker_tab.check_date_and_time_inputs()
        assert check_date_picker_tab, "Expected proper dates chosen, got wrong dates instead"

    @allure.description("This test opens menus and clicks all buttons in it")
    @pytest.mark.usefixtures("setup_for_menu_tab")
    def test_menu_tab(self, menu_tab):
        check_menu_tab = menu_tab.click_all_items()
        assert check_menu_tab, "Expected all menu buttons clicked, got no clickable buttons instead"

    @allure.description("This test starts the progress bar and checks if progress completed successfully")
    @pytest.mark.usefixtures("setup_for_progress_bar_tab")
    def test_progress_bar_tab(self, progress_bar_tab):
        check_progress_bar_tab = progress_bar_tab.check_progress_bar()
        assert check_progress_bar_tab, "Expected bar successfully started, stopped, and finished, " \
                                       "got wrong progress parameters instead"

    @allure.description("This test presses selects and checks all selections pressed successfully")
    @pytest.mark.usefixtures("setup_for_select_menu_tab")
    def test_select_menu_tab(self, select_menu_tab):
        check_select_menu_tab = select_menu_tab.check_select_menus()
        assert check_select_menu_tab, "Expected all selections made, got not all selections instead"

    @allure.description("This test changes value of slider from minimal to maximum")
    @pytest.mark.usefixtures("setup_for_slider_tab")
    def test_slider_tab(self, slider_tab):
        check_slider_tab = slider_tab.slide_and_check_slider()
        assert check_slider_tab, "Expected slider working at all values, got not all values working instead"

    @allure.description("This test opens tabs from webpage and checks if its content appears")
    @pytest.mark.usefixtures("setup_for_tabs_page")
    def test_tabs_page(self, tabs_page):
        check_tabs_page = tabs_page.check_all_tubs()
        assert check_tabs_page, "Expected all buttons pressed and text appears, got no text appeared instead"

    @allure.description("This test hovers over contend and checks hoover presence")
    @pytest.mark.usefixtures("setup_for_tool_tips_tab")
    def test_tool_tips_tab(self, tool_tips_tab):
        check_tool_tips_tab = tool_tips_tab.check_hoovers_are_visible()
        assert check_tool_tips_tab, "Expected all hovers visible, got no hovers instead"
