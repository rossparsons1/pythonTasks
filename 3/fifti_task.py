import json

import pandas as pd
import requests
from bs4 import BeautifulSoup


def parse_products(url):
    data_list = []
    response = requests.get(url)

    # Проверяем статус ответа
    if response.status_code == 200:
        html_content = response.text

        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Извлекаем информацию о товарах
        products = soup.findAll('div', class_='product')  # Убедитесь, что класс правильный

        for product in products:
            item= {}
            item['id'] = product['id']
            item['title'] = product.find('span', class_='product__title').get_text().strip()
            item['price'] = float(product.find('span', class_='product__price').get_text().replace(" руб.", "").replace(" ", ""))
            data_list.append(item)
    else:
        print(f"Не удалось получить страницу. Статус код: {response.status_code}")

    return data_list


def analyze_data(df):
    sorted_df = df.sort_values(by='id')

    stats_views = {
        'sum': df['price'].sum(),
        'min': df['price'].min(),
        'max': df['price'].max(),
        'mean': df['price'].mean(),
        'count': df['price'].count()
    }

    frequency = df['title'].value_counts()

    return sorted_df, stats_views, frequency

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def save_df_to_json(df, output_file):
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)

def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return pd.DataFrame(data)


data_list = parse_products('https://creamshop.ru/store/clothing/?PAGEN_1=1')
save_to_json(data_list, 'output/output5.json')


data_list = []
for i in range(3):
    data_list.append(parse_products(f"https://creamshop.ru/store/clothing/bryuki/?PAGEN_1={i}"))
save_to_json(data_list, 'output/output_soloitem.json')


data_df = load_data_from_json("output/output5.json")
sorted_data, stats_views, frequency = analyze_data(data_df)
save_df_to_json(sorted_data, 'output/sorted_data5.json')
print(stats_views, frequency)