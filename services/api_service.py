import requests


class ApiService:

    BASE_URL = "https://petstore.swagger.io/v2"
    HEADERS = headers = {
            'accept': 'application/json',

            'Content-Type': 'application/json'
    }

    @staticmethod
    def _create_response_body(pet_id, pet_name):
        request_data = {
                "id": pet_id,
                "category": {
                                    "id": 0,
                                    "name": "string"
                                },
                "name": pet_name,
                "photoUrls": [
                              "string"
                             ],
                "tags": [
                            {
                                "id": 0,
                                "name": "string"
                            }
                        ],
                "status": "available"
                }
        return request_data

    def _create_general_url(self, endpoint):
        url = self.BASE_URL + endpoint
        return url

    def _get_request(self, endpoint):
        url = self._create_general_url(endpoint)
        response = requests.get(url)
        return response

    def _post_request(self, endpoint, request_body):
        url = self._create_general_url(endpoint)
        response = requests.post(url, headers=self.HEADERS, json=request_body)
        return response

    def _delete_request(self, endpoint):
        url = self._create_general_url(endpoint)
        response = requests.delete(url)
        return response

    def add_new_pet(self, id, pet_name):
        endpoint = "/pet"
        request_body = self._create_response_body(id, pet_name)
        response = self._post_request(endpoint, request_body)
        return response

    def get_pet_by_id(self, pet_id):
        endpoint = f"/pet/{pet_id}"
        response = self._get_request(endpoint)
        return response

    def delete_pet(self, pet_id):
        endpoint = f"/pet/{pet_id}"
        response = self._delete_request(endpoint)
        return response
