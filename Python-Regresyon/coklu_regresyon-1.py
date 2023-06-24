# pip install scikit-learn
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

data = pd.read_csv ("student-mat.csv", sep=",")

predict = "G3"
y = np.array(data[predict])

data = data [["G1", "G2", "studytime", "failures", "absences"]]

x = np.array(data)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = LinearRegression()
linear.fit(x_train,y_train)


print(linear.coef_)
print(linear.intercept_)

print("Elde edilen regresyon modeli: Y={} + {} G1 + {} G2 + {} StudyTime + {} Failures + {} Absences".format(linear.intercept_,
                            linear.coef_[0], linear.coef_[1], linear.coef_[2], linear.coef_[3], linear.coef_[4]))

y_predicted = linear.predict(x_train)
print("R kare değeri = ", r2_score(y_train,y_predicted))

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

