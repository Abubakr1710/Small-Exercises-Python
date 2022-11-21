# INSTRUCTIONS:
# 1. RUN THIS COMMAND IN YOUR TERMINAL: cd venv/Scripts/activate
# 2. In this project i used numpy, pandas, scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import metrics
# uncomment the following line if you want to see answers
# data = np.genfromtxt('lab4_reg6a.txt', delimiter='\t')
# print('DATA:')
# print(data) # uncomment to see the data
# print('Type of data:', type(data))
# print('SHAPE:', data.shape)
# print('Size:', data.size)

df = pd.read_csv('lab4_reg6a.txt', sep='\t', header=None)
#print(df) # uncomment to see the data
X,Y = df.iloc[:,0:6], df.iloc[:,-1]
#print(X.head()) # uncomment to see the features
#print(Y.head()) # uncomment to see the labels
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42) # Splitting the data into training and testing sets

model = LinearRegression() # Creating the model
model.fit(X_train,y_train) # Fitting the model

predictions = model.predict(X_test) # Predicting the test set
print('MAE:', metrics.mean_absolute_error(y_test, predictions)) # Mean Absolute Error
print('MSE:', metrics.mean_squared_error(y_test, predictions)) # Mean Squared Error

# Plotting the predictions
plt.scatter(y_test,predictions)
plt.show()

