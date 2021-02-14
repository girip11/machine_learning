# Participating in kaggle competitions

## Goals

* Focus is to learn and apply as much as possible.
* Actively read the kernels and discussion threads in the competition that you are competing.

## EDA on dataset

* Handle missing values
* Target distribution(balanced vs imbalanced dataset)
* Correlation between features

## Train and test set similarity

This can be found using the following approach.

* Combine training and test data leaving out the actual target column since this won't be present in the test data.
* Introduce a new target column and set it to 0 for all training instances and 1 for testing instances. We have now created a problem of predicting if a particular instance is from test or training set.
* Train an ML model on this dataset and evaluate with validation set(or perform cross validation).
* If ML model has AUC ROC more than 0.5 then the train and test data sets are different. If `<0.5`, then test and train datasets are similar.
* For tabular problems, its common for people to start with tree based models. LightGBM/XGBoost are often recommended.

## Model evaluation

* Its recommended to store model parameters and its validation score.

---

## References

* [How to Start Competing on Kaggle](https://towardsdatascience.com/how-to-begin-competing-on-kaggle-bd9b5f32dbbc)
