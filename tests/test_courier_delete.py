import pytest
import allure
import logging

from methods.courier_methods import CourierMethods
from data.messages import ERROR_MISSING_REQUIRED_FIELDS_TO_DEL, ERROR_COURIER_ID_NOT_FOUND

logger = logging.getLogger(__name__)


class TestCourierDelete:

    @allure.title("Успешное удаление курьера возвращает статус 201")
    def test_delete_courier_success(self, courier_id):
        with allure.step("Удаляем курьера"):
            response = CourierMethods.delete_courier(courier_id)

        with allure.step("Проверка статуса успешного создания 200"):
            assert response.status_code == 200, f"Ожидается статус 200, получен статус {response.status_code}"
        with allure.step("Проверка успешного сообщения"):
            logger.info(f"Курьер: {courier_id} удален из БД")
            assert response.json() == {"ok": True}

    @allure.title("Удаление курьера с несуществующим id вызывает ошибку 404")
    @pytest.mark.parametrize(
        "invalid_id",
        [
            0,
            999999,
        ]
    )
    def test_delete_courier_invalid_id_returns_error(self, invalid_id):
        with allure.step("Удаляем курьера"):
            response = CourierMethods.delete_courier(invalid_id)

        with allure.step("Проверка статуса ошибки 404"):
            assert response.status_code == 404, f"Ожидается статус 404, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ERROR_COURIER_ID_NOT_FOUND
            logger.info(f"{response.json()["message"]} - {invalid_id}")

    @allure.title("Удаление курьера без передачи id вызывает ошибку 400")
    def test_delete_courier_without_id_returns_error(self):
        with allure.step("Удаляем курьера"):
            response = CourierMethods.delete_courier("")

        with allure.step("Проверка статуса ошибки 400"):
            assert response.status_code == 400, f"Ожидается статус 400, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_MISSING_REQUIRED_FIELDS_TO_DEL
