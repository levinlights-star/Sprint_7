import allure
import logging

from methods.order_methods import OrderMethods
from data.messages import ERROR_MISSING_REQIRED_FOR_SEARCH, ERROR_COURIER_ID_NOT_FOUND_FOR_ACCEPT, ERROR_ORDER_NOT_FOUND_FOR_ACCEPT

logger = logging.getLogger(__name__)


class TestOrderAccept:
    @allure.title("Успешное принятие заказа курьером")
    def test_order_accept_success(self, courier_id, created_order, get_order_id, courier_id_for_cleanup, cancel_order_for_cleanup):
        response = OrderMethods.accept_order(get_order_id, courier_id)
        with allure.step("Проверка успешного принятия заказа курьером"):
            assert response.status_code == 200, f"Ожидается статус 200, получен статус {response.status_code}"
        with allure.step("Проверка успешного сообщения"):
            assert response.json() == {"ok": True}

    @allure.title("Ошибка при принятии заказа без указания id курьера")
    def test_order_accept_without_courier_id_returns_error(self, created_order, get_order_id, cancel_order_for_cleanup):
        courier_id = ''
        response = OrderMethods.accept_order(get_order_id, courier_id)
        with allure.step("Проверка статуса ошибки 400"):
            assert response.status_code == 400, f"Ожидается статус 400, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_MISSING_REQIRED_FOR_SEARCH

    @allure.title("Ошибка при принятии заказа без указания id заказа")
    def test_order_accept_without_order_id_returns_error(self, courier_id, courier_id_for_cleanup):
        get_order_id = ''
        response = OrderMethods.accept_order(get_order_id, courier_id)
        with allure.step("Проверка статуса ошибки 400"):
            assert response.status_code == 400, f"Ожидается статус 400, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_MISSING_REQIRED_FOR_SEARCH

    @allure.title("Ошибка при принятии заказа при несуществующем id заказа")
    def test_order_accept_with_incorrect_order_id_returns_error(self, courier_id, courier_id_for_cleanup):
        get_order_id = '999999'
        response = OrderMethods.accept_order(get_order_id, courier_id)
        with allure.step("Проверка статуса ошибки 404"):
            assert response.status_code == 404, f"Ожидается статус 404, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_ORDER_NOT_FOUND_FOR_ACCEPT

    @allure.title("Ошибка при принятии заказа при несуществующем id курьера")
    def test_order_accept_with_incorrect_courier_id_returns_error(self, created_order, get_order_id, cancel_order_for_cleanup):
        courier_id = '999999'
        response = OrderMethods.accept_order(get_order_id, courier_id)
        with allure.step("Проверка статуса ошибки 404"):
            assert response.status_code == 404, f"Ожидается статус 404, получен статус {response.status_code}"
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json()[
                "message"] == ERROR_COURIER_ID_NOT_FOUND_FOR_ACCEPT
