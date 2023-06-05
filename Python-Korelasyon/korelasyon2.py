# walmart verisinde 'Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment' arasındaki korelasyon
# https://wlmolina.github.io/dataset_2-2010_to_11-2012_Walmart_Store_sales.csv
import pandas as pd

walmart_veri = pd.read_csv('walmart_sales.csv')
walmart_veri = walmart_veri[['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature',
                             'Fuel_Price', 'CPI', 'Unemployment']]

print(walmart_veri)

secilen_veri = walmart_veri[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]

corr = secilen_veri.corr()

print(corr)