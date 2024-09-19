import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('belajar_python/freecodecamp/Data Analysis With Python/data/sales_data.csv', parse_dates=['Date'])

# print(sales.head())
print(sales.shape) #mengetahui jumlah baris dan kolom
print(sales.info())
print(sales.describe())
print(sales.dtypes)


sales['Month'] = sales['Month'].map({
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
})

sales = sales.select_dtypes(include=['number'])

sales = sales.dropna()  # Menghapus baris dengan nilai hilang
# atau
sales.fillna(0, inplace=True) 

print(sales.corr())