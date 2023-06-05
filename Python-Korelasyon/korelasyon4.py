# sadece weekly_sales değişkeni ile olan korelasyonları tek sütun halinde sıralı olarak gösterme
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

walmart_veri = pd.read_csv('walmart_sales.csv')
walmart_veri = walmart_veri[['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag', 'Temperature',
                             'Fuel_Price', 'CPI', 'Unemployment']]

#print(walmart_veri)

secilen_veri = walmart_veri[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]

#corr = secilen_veri.corr()
corr = secilen_veri.corr()[['Weekly_Sales']].sort_values(by='Weekly_Sales', ascending=False)

#sns.heatmap(corr, cmap='RdBu', vmin=-1, vmax=1, annot=True)
heatmap = sns.heatmap(corr, vmin=-1, vmax=1, annot=True, cmap='BrBG')

heatmap.set_title('Features Correlating with Weekly_Sales', fontdict={'fontsize':18}, pad=16);

plt.show()

#print(corr)