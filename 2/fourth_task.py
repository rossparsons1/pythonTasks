import pickle
import json


def update_prices(products, price_updates):
    for update in price_updates:
        item_name = update['name']
        method = update['method']
        param = update['param']

        for product in products:
            if product['name'] == item_name:
                if method == "add":
                    product['price'] += param
                elif method == "sub":
                    product['price'] -= param
                elif method == "percent+":
                    product['price'] *= (1 + param)
                elif method == "percent-":
                    product['price'] *= (1 - param)
                break

    return products


with open('data/fourth_task_products.json', 'rb') as pkl_file:
    products = pickle.load(pkl_file)

with open('data/fourth_task_updates.json', 'r', encoding='utf-8') as json_file:
    price_updates = json.load(json_file)

updated_products = update_prices(products, price_updates)

with open('data/products_updated.pkl', 'wb') as pkl_out:
    pickle.dump(updated_products, pkl_out)
