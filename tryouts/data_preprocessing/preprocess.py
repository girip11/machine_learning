# Import the required packages and modules
import os

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# from matplotlib import pyplot as plt

# importing the dataset
dataset_path = f"{os.path.dirname(__file__)}/Data.csv"
dataset = pd.read_csv(dataset_path)

# This will take all the columns from all the rows except
# the last column which is the dependent variable.
X = dataset.iloc[:, :-1].values
print(X)

# Take only the last column
y = dataset.iloc[:, -1].values
print(y)

# Taking care of missing data in the columns
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# We should pass only the columns with numerical values only.
imputer.fit(X[:, 1:3])

# transform and replace
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

# Encoding the categorical data
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")
# converting to numpy array because, ML models expect that in this form
X = np.array(ct.fit_transform(X))

print(X)

# Encoding the dependent variable
le = LabelEncoder()
# converts string values to integer labels
y = le.fit_transform(y)

print(y)

# Split data in to training and testing dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Feature scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
# feature scaling applied to numerical columns
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
# don't apply fit_transform on X_test, since it will
# consider mean and stddev of test dataset
X_test[:, 3:] = sc.transform(X_test[:, 3:])

print(X_train)
print(X_test)
