import pandas as pd

def process_csv():
    try:
        df = pd.read_csv("data/fourth_task.txt")

        if 'description' in df.columns:
            df.drop(columns=['description'], inplace=True)

        mean_rating = df['rating'].mean()

        max_price = df['price'].max()

        min_rating = df['rating'].min()

        filtered_df = df[df['category'] == 'Овощи']

        with open("data/fourth_task_out.txt", 'w', encoding='utf-8') as stats_file:
            stats_file.write(f'Среднее rating: {mean_rating}\n')
            stats_file.write(f'Mаксимум price: {max_price}\n')
            stats_file.write(f'Минимум rating: {min_rating}\n')

        filtered_df.to_csv("./data/fourth_task_out(csv).txt", index=False)

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к входному файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


process_csv()