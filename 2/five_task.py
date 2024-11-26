import pandas as pd
import json
import os

df = pd.read_csv('data/vct_data.csv')

selected_fields = ['u_credits', 't1_credits', 't2_credits', 't3_credits', 't4_credits', 'shield', 'gun']
df_selected = df[selected_fields]

numerical_stats = df_selected.describe(include='number').T
numerical_stats['sum'] = df_selected.sum(numeric_only=True)
numerical_stats['std'] = df_selected.std(numeric_only=True)

frequency_stats = df_selected['gun'].value_counts().to_dict()

final_stats = {
    'numerical_stats': numerical_stats.to_dict(orient='index'),
    'categorical_stats': frequency_stats,
}

with open('statistics.json', 'w', encoding='utf-8') as json_file:
    json.dump(final_stats, json_file, ensure_ascii=False, indent=4)

df_selected.to_csv('data/vct_selected.csv', index=False)
df_selected.to_json('data/vct_selected.json', orient='records', lines=True, force_ascii=False)
df_selected.to_pickle('data/vct_selected.pkl')
df_selected.to_parquet('data/vct_selected.parquet')

files = ['data/vct_selected.csv', 'data/vct_selected.json', 'data/vct_selected.pkl', 'data/vct_selected.parquet']
sizes = {file: os.path.getsize(file) for file in files}

for file, size in sizes.items():
    print(f'Размер файла {file}: {size} байт')
