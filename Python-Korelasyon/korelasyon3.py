# pip install seaborn
# pip install matplotlib
# walmart verisi korelasyon değerlerini heatmap ile grafik olarak gösterme
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

walmart_veri = pd.read_csv('walmart_sales.csv')
walmart_veri = walmart_veri[['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature',
                             'Fuel_Price', 'CPI', 'Unemployment']]

print(walmart_veri)

secilen_veri = walmart_veri[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]

corr = secilen_veri.corr()

sns.heatmap(corr, cmap='RdBu', vmin=-1, vmax=1, annot=True)

plt.show()

