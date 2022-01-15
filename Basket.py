
from Parts import *

header = ['Client', 'ID of part - Compatible models', 'Date of Order', 'Price']


class ShoppingCart:
    current_date_now = datetime.now()
    dt_str = current_date_now.strftime("%d-%m-%Y %H:%M:%S")

    def __init__(self, cart_item, customer_id='none', current_date=dt_str):
        self.customer_id = customer_id
        self.current_date = current_date
        self.cart_item = cart_item


