import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("./Housing.csv")

data = df[['price','area','bedrooms','bathrooms','airconditioning','furnishingstatus']]

data['airconditioning'] = data['airconditioning'].replace(("yes","no"),(1,0))
data['furnishingstatus'] = data['furnishingstatus'].replace(("furnished","semi-furnished","unfurnished"),(1,0.5,0))

X = data.drop(columns = ['price'])
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

lr = LinearRegression()
lr.fit(X_train, y_train)

pickle.dump(lr,open('model.pkl','wb'))