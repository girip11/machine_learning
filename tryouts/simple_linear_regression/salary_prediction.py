# imports
# import numpy as np
import os

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# read the dataset
dataset_path = f"{os.path.dirname(__file__)}/Salary_Data.csv"
dataset = pd.read_csv(dataset_path)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# train and test data set split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# training the simple linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test results
predicted_values = regressor.predict(X_test)
print(X_test)
print(list(zip(predicted_values, y_test)))

# visualizing training set results
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# visualizing test set results
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary vs Experience (Testing set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# predict single input
salary = regressor.predict([[12]])
print(salary)

# get the slope and intercept
print(regressor.coef_)  # slope
print(regressor.intercept_)  # intercept
