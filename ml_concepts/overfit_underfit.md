# Overfitting and Underfitting

In statistics, fit refers to how well we approximate the target function. Target function refers to the values of the dependent variable.

> Supervised machine learning is best understood as approximating a target function (f) that maps input variables (X) to an output variable (Y). `Y = f(X)`

* Training dataset represents a sample from the population. The training dataset contains features of the population as well as some noise.

## Generalization

* Generalization - learning generalized concepts from a specific sample(training data).
* Supervised learning models use inductive learning (i.e) using the characteristics of training dataset to predict the outcome of the new unseen data.

## Underfitting

* Underfitting refers to a model that does not approximate the target function well. Such a model will have low coefficient of determination.

* In such cases, alternate machine learning algorithms can be explored that would better approximate the target function.

## Overfitting

* Overfitting refers to model that has learnt the known data (training data) very well. Such a model will have a **high coefficient of determination** for the training dataset.
* When fitting the training data very well, we also pick up the noisy features which could decrease the generalization and hence the model performance on the unseen dataset.

> Overfitting is more likely with nonparametric and nonlinear models that have more flexibility when learning a target function.

## Limit overfitting

* Resampling techniques. Popular resampling technique is **k-fold cross validation**.
* Hold back a part of training dataset as validation dataset

---

## References

* [Overfitting and underfitting](https://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/)
