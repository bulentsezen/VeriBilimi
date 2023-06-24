# pip install statsmodels
import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv ("student-mat.csv", sep=",")
predict = "G3"
y = np.array(data[predict])

data = data [["G1", "G2", "studytime", "failures", "absences"]]

X = np.array(data)

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())