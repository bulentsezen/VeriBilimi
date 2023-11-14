import numpy as np
from scipy import stats

# ölçülen süt mililitre değeri
mililitre1 = np.array([990, 999, 998, 990, 999, 990, 991, 990, 990, 980])
mililitre2 = np.array([1005, 1002, 1003, 999, 1005, 1000, 1001, 1000, 997, 1002])

# İki bağımsız örneklem (two-sample) t-test uygulaması:
t_stat, p_value = stats.ttest_ind(mililitre1, mililitre2)
print("T statistic:", t_stat)
print("P-value:", p_value)

# Anlamlılık seviyesi:
alpha = 0.01

# sonuçları yazdırma
if p_value < alpha:
    print("iki örneklem ortalamaları arasında önemli bir fark vardır. Anlamlılık seviyesi: ", alpha)
else:
    print("iki örneklem ortalamaları arasında önemli bir fark vardır. Anlamlılık seviyesi: ", alpha)
