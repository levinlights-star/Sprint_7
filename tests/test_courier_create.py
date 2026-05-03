import pytest
import allure
import logging

from methods.courier_methods import CourierMethods
from data.messages import ERROR_DUPLICATE_COURIER, ERROR_MISSING_REQUIRED_FIELDS

logger = logging.getLogger(__name__)


class TestCourierCreate:

    @allure.title("Успешное создание курьера возвращает статус 201")
    def test_create_courier_success(self, courier_data):
        with allure.step("Создание курьера"):
            response = CourierMethods.create_courier(courier_data)
        logger.info(f"Сгенерированные данные: {courier_data}")
        with allure.step("Проверка статуса успешного создания 201"):
            assert response.status_code == 201,  f"Ожидается статус 201, получен статус {response.status_code}"
        with allure.step("Проверка успешного сообщения"):
            assert response.json() == {"ok": True}

    @allure.title("Создание дубликата курьера возвращает ошибку 409")
    def test_create_courier_duplicate(self, courier_data, courier_id_for_cleanup):
        with allure.step("Создание курьера"):
            response = CourierMethods.create_courier(courier_data)
        logger.info(f"Сгенерированные данные: {courier_data}")

        with allure.step("Попытка создать дубликат курьера"):
            duplicate_response = CourierMethods.create_courier(courier_data)

        with allure.step("Проверка статуса ошибки 409"):
            assert duplicate_response.status_code == 409, f"Ожидается статус 409, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке дубликата"):
            assert duplicate_response.json(
            )["message"] == ERROR_DUPLICATE_COURIER

    @allure.title("Создание курьера без обязательных полей возвращает 400")
    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param(
                {}, id="all_fields_empty"),
            pytest.param(
                {"password": "mypass", "firstName": "test"}, id="empty_login"),
            pytest.param(
                {"login": "mylogin", "firstName": "test"}, id="empty_password"),
        ]
    )
    def test_create_courier_without_required_fields_returns_error(self, payload):
        with allure.step("Создание курьера"):
            response = CourierMethods.create_courier(payload)
        with allure.step("Проверка статуса ошибки 400"):
            assert response.status_code == 400, f"Ожидается статус 400, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке о нехватке данных"):
            assert response.json()[
                "message"] == ERROR_MISSING_REQUIRED_FIELDS
