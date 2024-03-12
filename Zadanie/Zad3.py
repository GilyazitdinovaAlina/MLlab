from Utils import uti


def print_max_mean_min(name, col):
    print('Столбец - ' + name)
    print('Максимальное: ' + str(col.max()))
    print('Минимальное:  ' + str(col.min()))
    print('Среднее:      ' + str(col.mean()) + '\n')

#Для каждого ключа и значения из словаря, преобразованного из data_frame в серии,
# вызывается функция print_max_mean_min, которая выводит информацию о максимальном, минимальном и среднем значении каждого столбца.
def exec_task(data_frame):
    [print_max_mean_min(key, value) for key, value in data_frame.to_dict('series').items()]
    uti.print_success(3)