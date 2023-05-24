import csv
import os

data_folder = "data/"

files = os.listdir(data_folder)
encabezado = ["Fecha", "Hora"]


def open_csv(file_name):
    with open(file=file_name, mode='rt', encoding="utf8") as f:
        filas = csv.reader(f, delimiter=";")
        list_temp = [{name: i for name, i in zip(encabezado, fila)} for n_fila, fila in enumerate(filas, start=1)]

    return list_temp


files_list = [open_csv(data_folder+n) for n in files]
#print(f'Una lista de diccionarios:\n{files_list}')

longitudes = [len(lista) for n, lista in enumerate(files_list)]
print(f'longitudes: {longitudes}')

filas_vacias = [{n_row: row for n_row, row in enumerate(lista)} for n, lista in enumerate(files_list)]
otras_longitudes = [len(lista_vacios) for n, lista_vacios in enumerate(filas_vacias)]
print(f'filas vacias: {otras_longitudes}')