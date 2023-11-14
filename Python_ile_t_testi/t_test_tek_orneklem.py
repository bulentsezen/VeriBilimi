import numpy as np
from scipy import stats

# ölçülen süt mililitre değeri
mililitre = np.array([999, 999, 998, 999, 999, 1001, 1002, 999, 999, 1000])


# olması gereken 1000 mililitre ortalama değeri
ortalama = 1000

# Tek örneklem (one-sample) t-test uygulaması
t_stat, p_value = stats.ttest_1samp(mililitre, ortalama)
print("T statistic:", t_stat)
print("P-value:", p_value)

# Anlamlılık seviyesi
alpha = 0.05

# sonuçları yazdırma
if p_value < alpha:
    print("örneklem ortalaması ile varsayılan popülasyon ortalaması arasında önemli bir fark vardır. Anlamlılık seviyesi: ", alpha)
else:
    print("örneklem ortalaması ile varsayılan popülasyon ortalaması arasında önemli bir fark yoktur. Anlamlılık seviyesi: ", alpha)
