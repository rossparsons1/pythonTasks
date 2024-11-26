import json
import msgpack
import os
def aggregate_product_info(products):
    aggregated_info = []

    for product in products:
        if 'name' in product and 'price' in product:
            price = product['price']
            aggregated_info.append({
                'product_name': product['name'],
                'average_price': price,
                'max_price': price,
                'min_price': price
            })
        else:
            print(f"Недостаточные данные для товара: {product}")

    return aggregated_info

with open('data/third_task.json', 'r', encoding='utf-8') as json_file:
    products = json.load(json_file)

aggregated_data = aggregate_product_info(products)

with open('data/aggregated_products.json', 'w', encoding='utf-8') as json_out:
    json.dump(aggregated_data, json_out, ensure_ascii=False, indent=4)

with open('data/aggregated_products.msgpack', 'wb') as msgpack_out:
    packed_data = msgpack.packb(aggregated_data)
    msgpack_out.write(packed_data)

size_json = os.path.getsize('data/aggregated_products.json')
size_msgpack = os.path.getsize('data/aggregated_products.msgpack')

print(f'Размер файла aggregated_products.json: {size_json} байт')
print(f'Размер файла aggregated_products.msgpack: {size_msgpack} байт')
