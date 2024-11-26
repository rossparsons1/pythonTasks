import numpy as np
import json

matrix = np.load('data/first_task.npy')

total_sum = matrix.sum()

average = matrix.mean()

sum_main_diagonal = np.trace(matrix)
average_main_diagonal = sum_main_diagonal / matrix.shape[0]

sum_secondary_diagonal = np.trace(np.fliplr(matrix))
average_secondary_diagonal = sum_secondary_diagonal / matrix.shape[0]

max_value = matrix.max()
min_value = matrix.min()

result = {
    'sum': total_sum.item(),
    'avr': average.item(),
    'sumMD': sum_main_diagonal.item(),
    'avrMD': average_main_diagonal.item(),
    'sumSD': sum_secondary_diagonal.item(),
    'avrSD': average_secondary_diagonal.item(),
    'max': max_value.item(),
    'min': min_value.item()
}

with open('data/first_task_out.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)
