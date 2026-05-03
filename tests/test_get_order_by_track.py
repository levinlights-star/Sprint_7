import pytest
import allure
import logging

from methods.order_methods import OrderMethods

from data.messages import ERROR_ORDER_TRACK_NOT_FOUND, ERROR_MISSING_REQUIRED_FOR_GET_ORDER


logger = logging.getLogger(__name__)


class TestGetOrderByTrack:
    @allure.title("Успешное получение заказа по его track")
    def test_get_order_by_track_success(self, created_order, cancel_order_for_cleanup):
        with allure.step("Отправить запрос на получение списка заказов"):
            response = OrderMethods.get_order_by_track(created_order)
        with allure.step("Проверка успешного получения списка заказов 200"):
            assert response.status_code == 200, f"Ожидается статус 200, получен статус {response.status_code}"

        with allure.step("Проверка структуры тела ответа"):
            data = response.json()
        assert "order" in data, "В ответе отсутствует ключ 'order'"
        assert isinstance(
            data["order"], dict), "Поле 'order' должно быть объектом"
        assert data["order"]["id"] is not None, "ID заказа не может быть пустым"

    @allure.title("Ошибка получения заказа с несуществующим track-номера")
    def test_get_order_by_incorrect_track_returns_error(self):
        with allure.step("Отправить запрос на получение списка заказов"):
            response = OrderMethods.get_order_by_track('999999')

        with allure.step("Проверка статуса ошибки 404"):
            assert response.status_code == 404, f"Ожидается статус 404, получен статус {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()["message"] == ERROR_ORDER_TRACK_NOT_FOUND

    @allure.title("Ошибка получения заказа без track-номера")
    def test_get_order_without_track_returns_error(self):
        with allure.step("Отправить запрос на получение списка заказов без track-номера"):
            response = OrderMethods.get_order_by_track('')

        with allure.step("Проверка статуса ошибки 400"):
            assert response.status_code == 400, f"Ожидается статус 400, получен статус {response.status_code}"

        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_MISSING_REQUIRED_FOR_GET_ORDER
