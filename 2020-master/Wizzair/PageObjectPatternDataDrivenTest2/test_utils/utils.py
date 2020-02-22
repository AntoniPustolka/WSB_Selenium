# pobieranie danych z pliku
import os
import csv

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    # Pomijam pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows
