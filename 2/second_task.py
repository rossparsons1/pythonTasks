import numpy as np
import os

matrix = np.load('data/second_task.npy')

indices = np.argwhere(matrix > 531)

x = indices[:, 0]
y = indices[:, 1]

values = matrix[matrix > 531]

z = values

np.savez('data/second_task_out.npz', x=x, y=y, z=z)

np.savez_compressed('data/second_task_out_compressed.npz', x=x, y=y, z=z)

size_npz = os.path.getsize('data/second_task_out.npz')
size_npz_compressed = os.path.getsize('data/second_task_out_compressed.npz')

print(f'Размер файла second_task_out.npz: {size_npz} байт')
print(f'Размер файла second_task_out_compressed.npz: {size_npz_compressed} байт')