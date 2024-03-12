from Utils import uti

#Создается новый DataFrame new_data_frame, который содержит строки, где значения в столбцах 'x1' и 'x2' меньше средних значений 'x1' и 'x2'.
# Функция .any(axis=1) возвращает True, если хотя бы одно условие выполняется для каждой строки данных.
def exec_task(data_frame, path):
    new_data_frame = data_frame[data_frame[['x1','x2']] < data_frame[['x1','x2']].mean()].any(axis=1)
    uti.print_success(4)
    new_data_frame.to_csv(path)