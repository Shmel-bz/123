import configuration
import requests

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)


def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}{configuration.GET_ORDER_PATH}{track_number}"
    response = requests.get(get_order_url)
    return response