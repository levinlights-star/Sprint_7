import pytest
import allure
import logging

from methods.courier_methods import CourierMethods
from data.messages import ERROR_MISSING_REQUIRED_FIELDS_TO_ENTER, ERROR_ACCOUNT_NOT_FOUND

logger = logging.getLogger(__name__)


class TestCourierAuth:

    @allure.title("Успешная авторизация возвращает статус 200")
    def test_login_courier_success(self, created_courier, courier_id_for_cleanup):
        response, courier_data = created_courier
        with allure.step("Авторизация курьера"):
            response = CourierMethods.login_courier(
                courier_data["login"],
                courier_data["password"]
            )

        with allure.step("Проверка статуса успешной авторизации 200"):
            assert response.status_code == 200,  f"Ожидается статус 200, получен статус {response.status_code}"
        with allure.step("Проверка получения id курьера"):
            assert "id" in response.json()

    @allure.title("Авторизация курьера без обязательных полей возвращает 400")
    @pytest.mark.parametrize(
        "login, password",
        [
            pytest.param("", "mypass", id="empty_login"),
            pytest.param("mylogin", "", id="empty_password"),
        ]
    )
    def test_login_courier_without_required_fields_returns_error(self, login, password):
        with allure.step("Авторизация курьера"):
            response = CourierMethods.login_courier(login, password)

        with allure.step("Проверка статуса ошибки 400"):
            assert response.status_code == 400, f"Ожидается статус 400, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке о нехватке данных"):
            assert response.json()[
                "message"] == ERROR_MISSING_REQUIRED_FIELDS_TO_ENTER

    @allure.title("Авторизация несуществующего курьера возвращает 404")
    def test_login_unregister_courier_returns_error(self):
        with allure.step("Авторизация курьера"):
            response = CourierMethods.login_courier("999999", "password")

        with allure.step("Проверка статуса ошибки 404"):
            assert response.status_code == 404, f"Ожидается статус 404, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_ACCOUNT_NOT_FOUND
