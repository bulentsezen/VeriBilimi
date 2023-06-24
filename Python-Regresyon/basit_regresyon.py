import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

veriseti = pd.read_csv('linear_model.csv')
print(veriseti.head())

print(veriseti.isnull().sum())

veriseti.y.fillna(value=veriseti.y.mean(), inplace=True)

print(veriseti.describe())

veriseti.x = (veriseti.x - veriseti.x.min() )/ (veriseti.x.max() - veriseti.x.min())
veriseti.y = (veriseti.y - veriseti.y.min() )/ (veriseti.y.max() - veriseti.y.min())

X = veriseti.x
y = veriseti.y

plt.scatter(X.values,y.values)
plt.xlabel('x')
plt.ylabel('Y')
plt.title('X y arasındaki ilişki')
plt.show()

lineer_regresyon = LinearRegression()
lineer_regresyon.fit(X.values.reshape(-1,1),y.values.reshape(-1,1))

print(lineer_regresyon.intercept_)
print(lineer_regresyon.coef_)

print("Elde edilen regresyon modeli: Y={}+{}X".format(lineer_regresyon.intercept_,lineer_regresyon.coef_[0]))

y_predicted = lineer_regresyon.predict(X.values.reshape(-1,1))
print("R kare değeri=", r2_score(y,y_predicted))

print("Ortalama Mutlak Hata: {} \nOrtalama Karesel Hata: {}".format(
    mean_absolute_error(y, y_predicted), mean_squared_error(y, y_predicted)))

def rmse(targets, predictions):
    return np.sqrt(((predictions - targets) ** 2).mean())
print("RMSE değeri: {}".format(rmse(y.ravel(),y_predicted.ravel())))

random_x = np.array([0, 0.5, 0.99])
plt.scatter(X.values, y.values)
plt.plot(random_x,
         lineer_regresyon.intercept_[0] +
         lineer_regresyon.coef_[0][0] * random_x,
         color='red',
         label='regresyon grafiği')
plt.xlabel('x')
plt.ylabel('Y')
plt.title('X y regresyon analiz')
plt.show()