import matplotlib.pyplot as plt
import numpy as np
from Utils import uti
import math


def exec_task(data_frame, path):
    fig = plt.figure(figsize=(10, 10))
    ax_3d = fig.add_subplot(projection='3d')
    ax_3d.scatter(data_frame['x1'], data_frame['x2'], data_frame['y'], c='r', marker='o')  # разноцветные точки

    # Создание координатной сетки для построения поверхности
    x1_min, x1_max = data_frame['x1'].min(), data_frame['x1'].max()
    x2_min, x2_max = data_frame['x2'].min(), data_frame['x2'].max()
    x1_vals = np.linspace(x1_min, x1_max, 100)
    x2_vals = np.linspace(x2_min, x2_max, 100)
    X1_vals, X2_vals = np.meshgrid(x1_vals, x2_vals)

    # Вычисление значений функции для каждой точки сетки
    Y_vals = np.zeros_like(X1_vals)
    for i in range(len(x1_vals)):
        for j in range(len(x2_vals)):
            Y_vals[i, j] = math.log(X1_vals[i, j]) * math.log(2 * X2_vals[i, j])

    # Построение поверхности
    ax_3d.plot_surface(X1_vals, X2_vals, Y_vals, cmap='viridis')

    plt.savefig(path)
    uti.print_success(5)