import pytest
import allure


class TestElementsPage:

    @allure.description("This test sends text to text boxes and checks if confirmation appears")
    @pytest.mark.usefixtures("setup_for_text_box")
    def test_text_box_tab(self, text_box):
        presence_of_confirmation = text_box.wait_for_confirmation()
        assert presence_of_confirmation, "Expected confirmation appearance, got no confirmation"

    @allure.description("This test clicks checkboxes and counts activated checkboxes")
    @pytest.mark.usefixtures("setup_for_check_box")
    def test_check_box_tab(self, check_box):
        active_elements_count = check_box.count_active_elements()
        assert active_elements_count == 17, f"Expected 17 active elements, got {active_elements_count} instead"

    @allure.description("This test clicks radio buttons and checks if all radio buttons are pressed")
    @pytest.mark.usefixtures("setup_for_radio_button")
    def test_radio_button_tab(self, radio_button):
        check_radio_button = radio_button.click_and_check_buttons()
        assert check_radio_button, "Expected all buttons pressed , not every button was pressed instead"

    @allure.description("This test sends information about new user, and checks if new user successfully created")
    @pytest.mark.usefixtures("setup_for_web_tables")
    def test_web_tables_tab(self, web_tables):
        check_web_tables = web_tables.input_information_and_check_new_user_created()
        assert check_web_tables, "Expected new user created, got no new user instead instead"

    @allure.description("This test presses every button on the page and checks if all buttons are pressed")
    @pytest.mark.usefixtures("setup_for_buttons_tab")
    def test_buttons_tab(self, buttons_tab):
        check_all_buttons_pressed = buttons_tab.click_and_check_buttons()
        assert check_all_buttons_pressed, "Expected all buttons pressed , not every button was pressed instead"

    @allure.description("This test uploads and downloads file from website and checks if file uploaded and downloaded")
    @pytest.mark.usefixtures("setup_for_upload_and_download_tab")
    def test_upload_and_download_tab(self, upload_and_download):
        check_all_buttons_pressed = upload_and_download.check_file_uploaded_and_downloaded()
        assert check_all_buttons_pressed, "Expected files uploaded and downloaded," \
                                          " no files uploaded or downloaded instead"

    @allure.description("This test clicks links and checks if new tabs and windows are opened")
    @pytest.mark.usefixtures("setup_for_links_tab")
    def test_links_tab(self, links_page):
        check_links = links_page.click_and_check_links()
        assert check_links, "Expected all links are working, got links not working instead"

    @allure.description("This test checks proper response from broken links")
    @pytest.mark.usefixtures("setup_for_broken_link_tab")
    def test_broken_links_tab(self, broken_link_tab):
        check_links = broken_link_tab.check_links()
        assert check_links, "Expected proper functionality, got wrong response instead"

    @allure.description("This test checks dynamic properties changed")
    @pytest.mark.usefixtures("setup_for_dynamic_properties")
    def test_dynamic_properties_tab(self, dynamic_properties):
        result_dynamic_properties = dynamic_properties.check_dynamic_properties()
        assert result_dynamic_properties, "Expected dynamic properties working as described, got wrong actions instead"
