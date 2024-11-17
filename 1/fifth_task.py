import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

def extract_table_to_csv():
    try:
        with open("data/fifth_task.html", 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        tables = soup.find_all('table')

        if not tables:
            print("Таблицы не найдены в HTML файле.")
            return

        table = tables[0]
        table_html = str(table)
        df = pd.read_html(StringIO(table_html))[0]

        df.to_csv("./data/fifth_task_out.txt", index=False, encoding='utf-8')


    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к входному файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

extract_table_to_csv()