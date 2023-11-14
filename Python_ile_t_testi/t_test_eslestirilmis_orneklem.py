import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ölçülen kilo değeri
onceki_kilo = np.array([90, 79, 98, 80, 89, 99, 77, 80, 90, 81, 75, 86, 69, 73, 80, 102, 98, 85, 76, 76, 81, 76, 78, 83, 87, 77, 98, 78, 77, 98, 104, 67, 75, 88, 84, 85, 69, 80, 84, 96, 69])
sonraki_kilo = np.array([90, 75, 97, 80, 88, 99, 73, 80, 90, 80, 74, 86, 69, 73, 80, 102, 91, 85, 76, 71, 81, 76, 78, 82, 82, 77, 98, 78, 77, 98, 104, 67, 75, 88, 84, 85, 69, 80, 84, 96, 69])

n, bins, patches = plt.hist(onceki_kilo)
plt.show()

n, bins, patches = plt.hist(sonraki_kilo)
plt.show()

# İki eşleştirilmiş örneklem (paired-sample) t-test uygulaması:
t_stat, p_value = stats.ttest_rel(onceki_kilo, sonraki_kilo)
print("T statistic:", t_stat)
print("P-value:", p_value)

# Anlamlılık seviyesi:
alpha = 0.01

# sonuçları yazdırma
if p_value < alpha:
    print("iki örneklem arasında önemli bir fark vardır. Anlamlılık seviyesi: ", alpha)
else:
    print("iki örneklem arasında önemli bir fark yoktur. Anlamlılık seviyesi: ", alpha)
