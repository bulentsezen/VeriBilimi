# pip install scikit-learn
# pip install statsmodels
from sklearn import datasets, linear_model
import statsmodels.api as sm

diabetes = datasets.load_diabetes()
#print(diabetes)
X = diabetes.data
y = diabetes.target

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

# p-value 0.01 den küçük ise model anlamlı %99
# p-value 0.05 den küçük ise model anlamlı %95