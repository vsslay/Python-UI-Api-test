from QAtools.services.api_service import ApiService
import allure


class TestApi(ApiService):

    @allure.description("This test add pet")
    def test_add_pet(self):
        response = self.add_new_pet(100, "duck")

        assert response.status_code == 200, f"Expected status code of server 200 but was {response.status_code}"

    @allure.description("This test checks the presence of pet by id")
    def test_check_pet_by_id(self):
        response = self.get_pet_by_id(100)

        assert response.status_code == 200, f"Expected status code of server 200 but was {response.status_code}"

    @allure.description("This test removes the presence of pet by id")
    def test_delete_pet(self):
        response = self.delete_pet(100)

        assert response.status_code == 200, f"Expected status code of server 200 but was {response.status_code}"
