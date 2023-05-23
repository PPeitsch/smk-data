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
#print(files_list)
print(f'Una lista de diccionarios:\n{files_list}')
