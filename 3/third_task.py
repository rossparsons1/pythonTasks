import pandas as pd
from bs4 import BeautifulSoup
import os
import json


def parse_html_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                item = {}
                soup = BeautifulSoup(file, 'xml').star

                for el in soup:
                    if el.name is None:
                        continue
                    item[el.name] = el.get_text().strip()
                data_list.append(item)

                item['radius'] = int(item['radius'])
    return data_list


def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return pd.DataFrame(data)


def analyze_data(df):
    sorted_df = df.sort_values(by='name')

    filtered_df = df[df['constellation'] == 'Близнецы']

    stats_views = {
        'sum': filtered_df['radius'].sum(),
        'min': filtered_df['radius'].min(),
        'max': filtered_df['radius'].max(),
        'mean': filtered_df['radius'].mean(),
        'count': filtered_df['radius'].count()
    }

    frequency = filtered_df['spectral-class'].value_counts()

    return sorted_df, filtered_df, stats_views, frequency


def save_df_to_json(df, output_file):
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)


directory = './data/3'
data_list = parse_html_files(directory)
save_to_json(data_list, 'output/output3.json')

data_df = load_data_from_json("output/output3.json")
sorted_data, filtered_data, stats_views, frequency = analyze_data(data_df)
save_df_to_json(sorted_data, 'output/sorted_data3.json')
save_df_to_json(filtered_data, 'output/filtered_data3.json')

print(stats_views, frequency)
