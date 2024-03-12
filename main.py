from Zadanie import Zad1, Zad2, Zad3, Zad4, Zad5
from Utils import const

data_frame = Zad1.exec_task(f'{const.CONST_DIR}test.csv')
Zad2.exec_task(data_frame, [
    f'{const.CONST_DIR}CONST_X1.png',
    f'{const.CONST_DIR}CONST_X2.png'
    ])
Zad3.exec_task(data_frame)
Zad4.exec_task(data_frame, f'{const.CONST_DIR}test2.csv')
Zad5.exec_task(data_frame, f'{const.CONST_DIR}3d_model.png')