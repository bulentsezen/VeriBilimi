import numpy as np
import pandas as pd
import scipy

np.random.seed(10)
# yaş aralığı verisini rassal olarak oluşturma
yas_araligi = np.random.choice(a= ["18-25","26-35","36-45","46-55","56-65", "66-75", "76-85"],
                              p = [0.05, 0.14 ,0.23, 0.05, 0.5, 0.02, 0.01],
                              size=1000)

# oy tercihleri verisini rassal olarak oluşturma
oy_tercihi = np.random.choice(a= ["A-Partisi","B-Partisi","C-Partisi"],
                              p = [0.4, 0.2, 0.4],
                              size=1000)
# veri yapısı (data frame) oluşturma
oy_verisi = pd.DataFrame({"yas":yas_araligi,
                       "oy":oy_tercihi})

# çarpraz tablo oluşturma
oy_verisi_tab = pd.crosstab(oy_verisi.yas, oy_verisi.oy, margins=True)

oy_verisi_tab.columns = ["A-Partisi", "B-Partisi", "C-Partisi", "satır_toplamı"]

oy_verisi_tab.index = ["18-25","26-35","36-45","46-55","56-65", "66-75", "76-85", "sütun_toplamı"]

gozlem = oy_verisi_tab.iloc[0:8, 0:4]

print(gozlem)

ki_kare_istatistik = scipy.stats.chi2_contingency(observed= gozlem)

print("Ki_kare istatistikleri: ", ki_kare_istatistik)

