# pip install scipy
# pearsonr fonksiyonu ile korelasyon katsayısı ve p-value hesaplama
import pandas as pd
from scipy.stats.stats import pearsonr
import numpy as np

walmart_veri = pd.read_csv('walmart_sales.csv', na_values='-')
walmart_veri = walmart_veri[['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature',
                             'Fuel_Price', 'CPI', 'Unemployment']]

x = walmart_veri[['Unemployment']]
y = walmart_veri[['Weekly_Sales']]
x1 = np.squeeze(x)
y1 = np.squeeze(y)
#print(x1,y1)
print(pearsonr(x1, y1))
