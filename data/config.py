BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
DELETE_COURIER = f"{BASE_URL}/api/v1/courier/"


CREATE_ORDER = f"{BASE_URL}/api/v1/orders"  # post
GET_ORDERS = f"{BASE_URL}/api/v1/orders"    # get
ACCEPT_ORDERS = f"{BASE_URL}/api/v1/orders/accept/"
GET_ORDERS_ID = f"{BASE_URL}/api/v1/orders/track"
CANCEL_ORDER = f"{BASE_URL}/api/v1/orders/cancel"
