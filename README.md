# Sprint_7

**Установка и запуск**
1. Клонируйте репозиторий
2. Установите зависимости: pip3 install -r requirements.txt (или pip install -r requirements.txt)
3. Запустите тесты: pytest
4. Для генерации отчёта Allure: pytest --alluredir=allure_results и allure serve allure_results

**Структура**
data/config - URL-ы
data/messages.py – текстовые сообщения API
methods/ – вспомогательные функции и генераторы данных
tests/ – тесты, разбитые по группам
pytest.ini – конфигурация pytest
