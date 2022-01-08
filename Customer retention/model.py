# https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# data load
data = pd.read_csv('customer_retention.csv')
data.sample(frac =1)
# data has already been preprocessed by me and the colab notebook is also uploaded
data['TotalCharges'].fillna(data['TotalCharges'].mean(), inplace=True)
# making columns
y = data['Discontinued']
X = data.drop('Discontinued', inplace=True, axis=1)

# model making
classifier = RandomForestClassifier()
classifier.fit(data, y)

# model saving
pickle.dump(classifier, open('model.pkl', 'wb'))

# viewing model
model = pickle.load(open('model.pkl', 'rb'))

print(model.predict([[0	, 0,	2	, 0,	0,	0,	0,	0,	0	, 0,	0,	53.85,	108.15]]))
print("model is working")
