import pandas as pd
from bs4 import BeautifulSoup
import os
import json


def parse_html_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            with open(os.path.join(directory, '1.html'), 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                builds = soup.find_all("a", attrs={'class': 'tc-item'})
                for build in builds:
                    print(build)
                    item = {}
                    # item['id'] = build.a['href']
                    item['server'] = build.div
                    # item['title'] = build.span.get_text().strip()
                    # item['price'] = float(build.price.get_text().replace("₽", "").replace(" ", "").strip())
                    # item['bonus'] = int(build.strong.get_text()
                    #                     .replace("+ начислим", "")
                    #                     .replace("бонусов", "")
                    #                     .strip())
                    # properties = build.ul.find_all("li")
                    # for prop in properties:
                    #     item[prop['type']] = prop.get_text().strip()
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

    filtered_df = df[df['sim'] == "2 SIM"]

    stats_views = {
        'sum': filtered_df['price'].sum(),
        'min': filtered_df['price'].min(),
        'max': filtered_df['price'].max(),
        'mean': filtered_df['price'].mean(),
        'count': filtered_df['price'].count()
    }

    city_frequency = filtered_df['title'].value_counts()

    return sorted_df, filtered_df, stats_views, city_frequency


def save_df_to_json(df, output_file):
    df.to_json(output_file, orient='records', lines=True, force_ascii=False)


directory = './data/5'
data_list = parse_html_files(directory)
save_to_json(data_list, 'output/output5.json')

# data_df = load_data_from_json("output/output2.json")
# sorted_data, filtered_data, stats_views, city_frequency = analyze_data(data_df)
# save_df_to_json(sorted_data, 'output/sorted_data2.json')
# save_df_to_json(filtered_data, 'output/filtered_data2.json')

# print(stats_views, city_frequency)