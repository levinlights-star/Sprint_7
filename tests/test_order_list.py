import allure
import logging

from methods.order_methods import OrderMethods

logger = logging.getLogger(__name__)


class TestOrderList:

    @allure.title("Список заказов возвращается в теле ответа")
    def test_get_orders_returns_orders_list(self):
        with allure.step("Отправить запрос на получение списка заказов"):
            response = OrderMethods.get_orders()

        with allure.step("Проверка успешного получения списка заказов 200"):
            assert response.status_code == 200, f"Ожидается статус 200, получен статус {response.status_code}"

        with allure.step("Проверка структуры тела ответа"):
            response_body = response.json()
            assert "orders" in response_body, "Ответ не содержит ключа 'orders'"
            assert isinstance(
                response_body["orders"], list), "Поле 'orders' должно быть списком (list)"
