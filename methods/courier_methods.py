import requests
import allure

from data.config import BASE_URL, CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER


class CourierMethods:

    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(
            f"{BASE_URL}{CREATE_COURIER}",
            json=payload
        )

    @staticmethod
    @allure.step("Залогиниться под курьером с логином: {login}")
    def login_courier(login, password):
        return requests.post(
            f"{BASE_URL}{LOGIN_COURIER}",
            json={
                "login": login,
                "password": password
            }
        )

    @staticmethod
    @allure.step("Удалить курьера по id: {courier_id}")
    def delete_courier(courier_id):
        return requests.delete(
            f"{BASE_URL}{DELETE_COURIER}{courier_id}"
        )
