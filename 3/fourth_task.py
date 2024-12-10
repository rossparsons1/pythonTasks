import pandas as pd
from bs4 import BeautifulSoup
import os
import json


def parse_html_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:

                soup = BeautifulSoup(file, 'xml').find_all('clothing')

                for el in soup:
                    item = {}
                    item['id'] = int(el.id.get_text())
                    item['name'] = el.find('name').get_text().strip()
                    item['category'] = el.category.get_text().strip()
                    item['size'] = el.size.get_text().strip()
                    item['color'] = el.color.get_text().strip()
                    item['material'] = el.material.get_text().strip()
                    item['price'] = float(el.price.get_text().strip())
                data_list.append(item)

    return data_list


def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return pd.DataFrame(data)


def analyze_data(df):
    sorted_df = df.sort_values(by='id')

    filtered_df = df[df['size'] == 'M']

    stats_views = {
        'sum': filtered_df['price'].sum(),
        'min': filtered_df['price'].min(),
        'max': filtered_df['price'].max(),
        'mean': filtered_df['price'].mean(),
        'count': filtered_df['price'].count()
    }

    frequency = filtered_df['category'].value_counts()

    return sorted_df, filtered_df, stats_views, frequency


def save_df_to_json(df, output_file):
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)


directory = './data/4'
data_list = parse_html_files(directory)
save_to_json(data_list, 'output/output4.json')

data_df = load_data_from_json("output/output4.json")
sorted_data, filtered_data, stats_views, frequency = analyze_data(data_df)
save_df_to_json(sorted_data, 'output/sorted_data4.json')
save_df_to_json(filtered_data, 'output/filtered_data4.json')

print(stats_views, frequency)
