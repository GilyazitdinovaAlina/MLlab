from Utils import uti, const
import matplotlib.pyplot as plt


def init_array_y_from_const(is_x1, array):
    return [uti.my_func(const.CONST_FOR_IMAGE, x) if is_x1 else uti.my_func(x, const.CONST_FOR_IMAGE) for x in array]

def create_plot(array_x, array_y, path):
    #Строится график на основе значений array_x и array_y.
    plt.plot(array_x, array_y)
    #Для каждой пары значений из array_x и array_y создается точечный график на графике.
    [plt.scatter(x, y, color='black', s=15, marker='.') for x, y in zip(array_x, array_y)]
    plt.savefig(path)

#Очищается текущий график
def clear_plot():
    plt.clf()

def exec_task(data_frame, paths):
    #Для каждого флага создается график на основе соответствующего массива array_x из data_frame и пути path для сохранения графика
    for flag, array_x, path in zip([True, False], [data_frame['x2'], data_frame['x1']], paths):
        array_y = init_array_y_from_const(flag, array_x)
        create_plot(array_x, array_y, path)
        clear_plot()

    uti.print_success(2)