import requests
import allure
import logging

from data.config import BASE_URL, CREATE_ORDER, GET_ORDERS, ACCEPT_ORDERS, GET_ORDERS_ID, CANCEL_ORDER
logger = logging.getLogger(__name__)


class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        return requests.post(CREATE_ORDER, json=payload)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders():
        return requests.get(GET_ORDERS)

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id: int, courier_id: int):
        result = requests.put(f"{ACCEPT_ORDERS}{order_id}", params={"courierId": courier_id})
        logger.info(f"id заказа: {order_id} принят курьером {courier_id} ")
        return result

    @staticmethod
    @allure.step("Получить заказ по его track")
    def get_order_by_track(order_track):
        return requests.get(GET_ORDERS_ID, params={"t": order_track})

    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(order_track):
        return requests.put(CANCEL_ORDER,
            json={
                "track": order_track
            }
        )
