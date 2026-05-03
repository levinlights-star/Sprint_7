import pytest
import allure
import logging

from methods.order_methods import OrderMethods
from data.order_data import BODY_ORDER

logger = logging.getLogger(__name__)


class TestOrderCreate:

    @allure.title("Успешное создание заказа возвращает 201 и номер заказа")
    @pytest.mark.parametrize(
        "color",
        [
            pytest.param(["grey"], id="one_color_grey"),
            pytest.param(["black"], id="one_color_black"),
            pytest.param([], id="empty_color"),
            pytest.param(["grey", "black"], id="two_color"),
        ]
    )
    def test_create_order_success(self, color):
        payload = {
            **BODY_ORDER,
            "color": color
        }

        with allure.step("Создание заказа"):
            response = OrderMethods.create_order(payload)

        with allure.step("Проверка успешного создания заказа"):
            assert response.status_code == 201, f"Ожидается статус 201, получен статус {response.status_code}"
        with allure.step("Проверка номера заказа"):
            logger.info(f"Номер заказа: {response.json()["track"]}")
            assert "track" in response.json(), "В ответе нет номера заказа (track)"
