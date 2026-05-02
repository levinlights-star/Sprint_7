import requests
import allure
import logging

from data.config import BASE_URL, CREATE_ORDER, GET_ORDERS, ACCEPT_ORDERS, GET_ORDERS_ID, CANCEL_ORDER
logger = logging.getLogger(__name__)


class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(
            f"{BASE_URL}{CREATE_ORDER}",
            json=payload
        )

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders():
        return requests.get(f"{BASE_URL}{GET_ORDERS}")

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id: int, courier_id: int):
        url = f"{BASE_URL}{ACCEPT_ORDERS}{order_id}"
        result = requests.put(url, params={"courierId": courier_id})
        logger.info(f"id заказа: {order_id} принят курьером {courier_id} ")
        return result

    @staticmethod
    @allure.step("Получить заказ по его track")
    def get_order_by_track(order_track):
        url = f"{BASE_URL}{GET_ORDERS_ID}"
        return requests.get(url, params={"t": order_track})

    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(order_track):
        return requests.put(
            f"{BASE_URL}{CANCEL_ORDER}",
            json={
                "track": order_track
            }
        )
