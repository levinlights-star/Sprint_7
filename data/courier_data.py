import random
import string
import allure

@allure.step("Генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@allure.step("Генерирует логин, пароль и имя курьера")
def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
