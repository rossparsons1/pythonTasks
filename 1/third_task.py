import numpy as np

def replace_na_with_mean(line):
    numbers = []
    for item in line.split():
        if item == "N/A":
            numbers.append(np.nan)
        else:
            numbers.append(float(item))

    for i in range(len(numbers)):
        if np.isnan(numbers[i]):
            start = max(i - 1, 0)
            end = min(i + 1, len(numbers) - 1)
            neighbors = [numbers[j] for j in range(start, end + 1) if not np.isnan(numbers[j])]
            if neighbors:
                numbers[i] = np.mean(neighbors)

    return numbers

def filter_data(numbers):
    return [x for x in numbers if x > 0 and np.sqrt(x) < 200]

def process_file():
    try:
        with open("data/third_task.txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()

        results = []

        for line in lines:
            numbers = replace_na_with_mean(line.strip())
            filtered_numbers = filter_data(numbers)
            results.append(filtered_numbers)

        with open("data/third_task_output.txt", 'w', encoding='utf-8') as out_file:
            for filtered in results:
                if filtered:
                    out_file.write(' '.join(map(str, filtered)) + '\n')
                else:
                    out_file.write('\n')

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к входному файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

process_file()