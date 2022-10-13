import pandas as pd


"""Given a file in excel, txt or csv format, it shows the first 5 lines of information
Vars:
    datos = contains the location of the file and the method to read it
Returns:
    5 first lines of data
"""
datos = pd.read_csv("C:/Users/Lennox/Desktop/data_prueba_tecnica.csv", header=None)
print(datos.head())
# you can also use: print(datos.values) in order to show the data
"""Extracted information, saves it to a specified file"""
datos.to_csv("C:/Users/Lennox/Desktop/saving_data.csv")