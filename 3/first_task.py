import pandas as pd
from bs4 import BeautifulSoup
import os
import json


def parse_html_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                builds = soup.find_all("div", attrs={'class': 'build-wrapper'})
                for build in builds:
                    item = {}
                    item['city'] = build.find_all("span")[0].get_text().split(":")[1].strip()
                    item['id'] = int(build.h1['id'])
                    item['type'] = build.h1.get_text().split(":")[1].strip()
                    address_temp = build.p.get_text().split("Улица:")[1].split("Индекс:")
                    item['address'] = address_temp[0].strip()
                    item['index'] = address_temp[1].strip()
                    item['floors'] = int(build.find_all("span", attrs={'class': 'floors'})[0].get_text().split(":")[1])
                    item['year'] = int(build.find_all("span", attrs={'class': 'year'})[0].get_text().split("Построено в")[1])
                    spans = build.find_all("span", attrs={'class': ''})
                    item['parking'] = spans[1].get_text().split(":")[1] == "есть"
                    item['rating'] = float(spans[2].get_text().split(":")[1])
                    item['views'] = int(spans[3].get_text().split(":")[1])

                    print(item)

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

    filtered_df = df[df['parking'] == True]

    stats_views = {
        'sum': filtered_df['views'].sum(),
        'min': filtered_df['views'].min(),
        'max': filtered_df['views'].max(),
        'mean': filtered_df['views'].mean(),
        'count': filtered_df['views'].count()
    }

    city_frequency = filtered_df['city'].value_counts()

    return sorted_df, filtered_df, stats_views, city_frequency


def save_df_to_json(df, output_file):
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)


directory = './data/1'
data_list = parse_html_files(directory)
save_to_json(data_list, 'output/output.json')

data_df = load_data_from_json("output/output.json")
sorted_data, filtered_data, stats_views, city_frequency = analyze_data(data_df)
save_df_to_json(sorted_data, 'output/sorted_data.json')
save_df_to_json(filtered_data, 'output/filtered_data.json')

print(stats_views, city_frequency)