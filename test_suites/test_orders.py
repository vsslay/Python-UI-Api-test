import allure
import pytest


@pytest.mark.usefixtures("setup_for_quantity_and_price_of_ducks")
class TestOrders:

    @allure.description("This test checks in the database whether the order has passed")
    def test_orders(self, cart_page, sql_service):
        initial_number_of_orders = sql_service.get_orders_id_count()
        cart_page.click_confirm_order()
        new_number_of_orders = sql_service.get_orders_id_count()
        assert new_number_of_orders == initial_number_of_orders + 1, "Zero orders found"
