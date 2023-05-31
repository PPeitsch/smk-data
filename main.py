import csv
import os
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from collections import Counter

data_folder = "data/"

files = os.listdir(data_folder)
encabezado = ["Fecha", "Hora"]


def open_csv(file_name):
    with open(file=file_name, mode='rt', encoding="utf8") as f:
        filas = csv.reader(f, delimiter=",")
        list_temp = [{name: i for name, i in zip(encabezado, fila)} for n_fila, fila in enumerate(filas, start=1)]

    return list_temp


files_list = [open_csv(data_folder + n) for n in files]

complete_list = [[row for n_row, row in enumerate(mlista) if not row['Fecha'] == ""]
                 for n, mlista in enumerate(files_list)]
result = [a for b in complete_list for a in b]

df = pd.DataFrame(result)
df['Hora'] = df['Hora'].str.replace("h", "")
df['Fecha'] = pd.to_datetime(df['Fecha'], format="%d/%m/%Y").dt.date

df['Hora'] = pd.to_datetime(df['Hora'], format="%H.%M").dt.time
df_sorted = df.sort_values(by=['Fecha'])
df_sorted = df_sorted.reset_index(drop=True)

a = df_sorted['Fecha'].duplicated()
df_sorted['n'] = a
df_sorted = df_sorted.drop('Hora', axis=1)
c = df_sorted.groupby('Fecha').count()

print(c)

c.index = pd.to_datetime(c.index)
#c = c.interpolate(method='cubic')
plt.figure(1)
plt.plot(c, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=5)
plt.show()
