import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree

data=pd.read_csv("diabetes.csv")

x=pd.DataFrame(data,columns=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"])
y=data.Outcome.values.reshape(-1,1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

clf=RandomForestClassifier(n_estimators=166,max_depth=8)

clf=clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

print("Accuracy :",metrics.accuracy_score(y_test,y_pred))

f_n=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
t_n=["0","1"]
fig=plt.figure(figsize=(60,20),dpi=100)
plot=tree.plot_tree(clf.estimators_[5],feature_names=f_n,class_names=t_n,filled=True)
fig.savefig("Tree1.png")