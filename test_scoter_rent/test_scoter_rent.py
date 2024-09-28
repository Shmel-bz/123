import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)
#захожу на курьера, и вижу что заказ добавился- скрин прилагается

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


# Автотест
def test_order_creation_and_retrieval():
    # Создание заказа
    response = create_order(data.order_body)
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}"  # Проверяем код ответа на создание

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

    # Получение данных заказа по треку
    order_response = get_order(track_number)

    # Проверки
    assert order_response.status_code == 200, f"Ошибка получения заказа: {order_response.status_code}"
    order_data = order_response.json()

    print("Данные заказа:")
    print(order_data)
#   pytest -rP посмотрим на номер заказа и информацию
## Шмелева Оксана, 22-я когорта — Финальный проект. Инженер по тестированию плюс



