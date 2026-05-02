import pytest
import allure
import logging

from data.courier_data import generate_courier_data
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from data.order_data import BODY_ORDER

logger = logging.getLogger(__name__)


@allure.title("Генерация данных курьера")
@pytest.fixture
def courier_data():
    return generate_courier_data()


@allure.title("Создание курьера")
@pytest.fixture
def created_courier(courier_data):
    response = CourierMethods.create_courier(courier_data)
    logger.info(f"Сгенерированные данные: {courier_data}")
    return response, courier_data


@allure.title("Получение id курьера")
@pytest.fixture
def courier_id(created_courier):
    response, courier_data = created_courier

    login_response = CourierMethods.login_courier(
        courier_data["login"],
        courier_data["password"]
    )
    id = login_response.json()["id"]
    logger.info(f"id курьера: {id}")
    return id


@allure.title("Удаление курьера по id")
@pytest.fixture
def courier_id_for_cleanup(courier_id):
    yield courier_id
    CourierMethods.delete_courier(courier_id)
    logger.info(f"Курьер {courier_id} удален из БД")


@allure.title("Создание заказа и получение его track")
@pytest.fixture
def created_order():
    payload = {
        **BODY_ORDER,
        "color": []
    }
    response = OrderMethods.create_order(payload)
    order_track = response.json().get("track")
    logger.info(f"Номер заказа (track): {order_track}")
    return order_track


@allure.title("Получение id заказа по его track")
@pytest.fixture
def get_order_id(created_order):
    response1 = OrderMethods.get_order_by_track(created_order)
    order_id = response1.json().get("order").get("id")
    logger.info(f"id заказа: {order_id}")
    return order_id


@allure.title("Отмена заказа по track-номеру")
@pytest.fixture
def cancel_order_for_cleanup(created_order):
    yield created_order
    OrderMethods.cancel_order(created_order)
    logger.info(f"Заказ с номером (track): {created_order} отменен")
