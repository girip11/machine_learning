# Handling Features with missing values

* Values of a feature can be missing at random or not random.

* Not Missing at Random(NMAR) -  When values are not missing randomly, then we might need to find out the reason/pattern that's causing the values to be missed. This could require domain knowledge of the problem we are trying to solve.

* Missing at Random(MAR) - When the values are missing at random, we can follow the below approaches to handle those instances and features.

## 1. Drops training instances

If some of the training instances have missing values and we have sufficiently large number of training instances, then we can drop these training instances with missing values.

But if we have only fewer instances, then we might want to tryout other approaches before dropping those.

## 2. Drop features with missing values

* Features with lots of missing values can be dropped.
* But sometimes we need to find out the feature importance of that feature before dropping it. We could take only those instances where the feature takes a valid value and find out its feature importance on that subset of the training set. If this feature seems to be highly important one, then we might need to find a value to impute its missing values.

## 3. Statistical imputation

* Fill the missing values with mean or median or mode or with some constant value.
* Use this for numerical features with missing values. Avoid this for encoded categorical features.

## 4. KNN Imputation

* Impute missing values based on values from its neighbours

## 5. [Iterative Imputation/Multivariate Imputation by Chained Equations](https://machinelearningmastery.com/iterative-imputation-for-missing-values-in-machine-learning/)

* This scikit implementation is inspired from MICE.

* MICE implementation is available in this [python package](https://github.com/iskandr/fancyimpute.)

* Each feature is modelled as function of other features. This way in one iteration every feature with missing values will become the target and other fields as its predictors.

* Once the first feature with missing values is imputed, the next feature becomes the target and its missing values are predicted based on other features.

## 6. Impute with Deep learning or machine learning

* This approach works very well for categorical and non numerical features.

* [Datawig](https://github.com/awslabs/datawig) is a library that has this implementation.

## 7. Maximum likelihood Imputation

## 8. Semi-supervised learning

* For instance using label propagation using K-means.

---

## References

* [Imputation techniques](https://www.kaggle.com/residentmario/simple-techniques-for-missing-data-imputation)
* [6 Different Ways to Compensate for Missing Values In a Dataset](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)
