import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("music.csv")

x = data.drop(columns=["genre"])
y = data["genre"]

model = DecisionTreeClassifier()
model.fit(x,y)

tahmin = model.predict([[21,1], [42,0]])
print(tahmin)