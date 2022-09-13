import pytest
import allure


class TestPracticeFormPage:

    @allure.description("This test fills registration form and checks if new user was created with proper information")
    @pytest.mark.usefixtures("setup_for_practice_form")
    def test_practice_form_tab(self, practice_form):
        check_practice_form = practice_form.input_information_and_check_confirmation()
        assert check_practice_form, "Expected form is fulfilled and confirmation window appears, " \
                                    "got no confirmation window instead"
