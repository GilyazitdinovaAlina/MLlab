from random import randint
import numpy as np
import pandas as pd
from Utils import uti
from Utils import const

#Создается словарь array, содержащий ключи "x1", "x2" и пустой список "y"
def init_array():
    array = {
        "x1": np.linspace(randint(1, 5), randint(6, 10), const.CONST_RANGE),
        "x2": np.linspace(randint(1, 5), randint(6, 10), const.CONST_RANGE),
        "y": []
    }

    array["y"] = [uti.my_func(x1, x2) for x1, x2 in zip(array["x1"], array["x2"])]

    return array

#DataFrame df сохраняется в CSV файл по указанному пути path
def save_data_frame(array, path):
    df = pd.DataFrame(array)
    df.to_csv(path)
    return df


def exec_task(path):
    # Создается массив array, вызывая функцию init_array(), которая генерирует данные для массива.
    array = init_array()
    data_frame = save_data_frame(array, path)
    #Выводится сообщение об успешном выполнении задачи.
    uti.print_success(1)
    return data_frame