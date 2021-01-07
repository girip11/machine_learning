# Preprocessing categorical data

* Feature encoding is used to tranform categorical feature in to a numerical variable.
* Categorical data can be ordinal or nominal
* Ordinal attributes are categorical attributes with a sense of order amongst the values.
* Nominal attributes consist of discrete categorical values with no notion or sense of order amongst them

## 1. LabelEncoding

Encode target variable to ordinal variable. Scikit-learn provides `sklearn.preprocessing.LabelEncoder`

## 2. OrdinalEncoding

Categorical feature to ordered numerical feature. `sklearn.preprocessing.OrdinalEncoder`

## 3. Frequency encoding

Categorical variable to a numerical variable by considering the frequency distribution of the data. Useful for nominal features.

## 4. Onehot encoding

Categorical feature to many boolean/binary features. `sklearn.preprocessing.OneHotEncoder`. Commonly used for nominal features

## 5. Dummy encoding

It is very similar to one hot encoding but here either the first or the last feature will be dropped. Suppose we have a nominal feature variable that contains 5 categories, then after dummy encoding and dropping first column(corresponding to the first category), we will end up having 4 new columns. These 4 columns will take values of either 0 or 1 to indicate the presence or absence of the category. All these new features will be 0, if the dropped category is present. You drop either the first of the last feature so as to avoid [dummy variable trap in statistics](./one_hot_encoding_pros_cons.ipynb).

## 6. Binary encoding

Suppose we have a nominal feature with 100 categories. Using one hot encoding we would have 100 new features. But we would need only 7 bits to represent 100. Thus in binary encoding, the categories are first encoded to integers and then those integers are converted to binary code with each bit becoming a new feature.

## 7. Effect encoding

Similar to dummy encoding, except 0 will be replaced with -1 indicating absence of that category.

## 8. Feature Hashing

Convert nominal feature with large number of categories to a fixed set of features(the number of the output features is a hyperparameter of the estimator). Scikit-learn provides `FeatureHasher` for this purpose.

```Python
from sklearn.feature_extraction import FeatureHasher

fh = FeatureHasher(n_features=6, input_type='string')
hashed_features = fh.fit_transform(vg_df['Genre'])
hashed_features.head()
```

**NOTE**- Binary encoder and target mean encoder can be found in the [category-encoders python package](https://pypi.org/project/category-encoders/)

## 9. Target (mean) Encoding

> Features are replaced with a blend of posterior probability of the target given particular categorical value and the prior probability of the target over all the training data

`TargetEncoder` is available in the package `category_encoders`.

* In case of multiclass classification or regression problems, replace categorical variable with the mean of the corresponding target variable. First group by categories and find the mean of the target variable for each category. Replace this mean as the value for its respective category. This can work for regression as well as classification.

* In case of binary classification, `total_instances_with_category_equals_1/total_instances_with_category`

* Refer to this notebook to [understand target encoding](./target_encoding.ipynb)

---

## References

* [Preprocessing categorical data](https://towardsdatascience.com/understanding-feature-engineering-part-2-categorical-data-f54324193e63)
* [Feature encoding](https://towardsdatascience.com/feature-engineering-deep-dive-into-encoding-and-binning-techniques-5618d55a6b38)
* [Deal with categorical features](https://www.kaggle.com/lucabasa/how-to-deal-with-categorical-features#From-continuous-to-categorical)
* [Target encoding](https://medium.com/analytics-vidhya/target-encoding-vs-one-hot-encoding-with-simple-examples-276a7e7b3e64)
