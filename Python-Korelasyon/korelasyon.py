# pip install pandas
# titanic verisinde 'Survived', 'Fare', 'Age' arasındaki korelasyon
# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
import pandas as pd

titanic_veri = pd.read_csv('titanic.csv')
titanic_veri = titanic_veri[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
                             'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]

print(titanic_veri)

secilen_veri = titanic_veri[['Survived', 'Fare', 'Age']]

corr = secilen_veri.corr()

print(corr)