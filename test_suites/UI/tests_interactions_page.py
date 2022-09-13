import pytest
import allure


class TestInteractionsPage:

    @allure.description("This test drags sortable elements and checks their position is proper")
    @pytest.mark.usefixtures("setup_for_sortable_tab")
    def test_sortable_tab(self, sortable_tab):
        sortable_tab_check = sortable_tab.drag_all_options()
        assert sortable_tab_check, "Expected proper position of all elements, got wrong positions instead"

    @allure.description("This test selects all elements and checks if all elements are selected")
    @pytest.mark.usefixtures("setup_for_selectable_tab")
    def test_selectable_tab(self, selectable_tab):
        selectable_tab_check = selectable_tab.choose_all_options()
        assert selectable_tab_check, "Expected all elements are selected, got not selected elements instead"

    @allure.description("This test resizes content boxes on page")
    @pytest.mark.usefixtures("setup_for_resizable_tab")
    def test_resizable_tab(self, resizable_tab):
        check_resizable_tab = resizable_tab.resize_all_boxes()
        assert check_resizable_tab, "Expected content boxes are resized, got wrong size of boxes instead"

    @allure.description("This test drag and drop elements on page")
    @pytest.mark.usefixtures("setup_for_droppable_tab")
    def test_droppable_tab(self, droppable_tab):
        check_droppable_tab = droppable_tab.drag_all_droppable_properties()
        assert check_droppable_tab, "Expected all draggable elements are dragged and dropped," \
                                    " got non-draggable elements instead"

    @allure.description("This test drags and drops elements to other elements and checks if drop-elements activated")
    @pytest.mark.usefixtures("setup_for_dragabble_tab")
    def test_dragabble_tab(self, dragabble_tab):
        check_dragabble_tab = dragabble_tab.drag_all_properties()
        assert check_dragabble_tab, "Expected all elements are dropped to proper elements," \
                                    " got not activated elements instead"
