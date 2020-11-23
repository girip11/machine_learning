# Stacking and blending explained

## Stacking

In stacking there can be many layers. In each layer, we can have a number of models, with each models backed up by different machine learning algorithms.

### Working of stacking using 3 layers

* Consider a classification problem, with first layer consisting of KNN, Logistic regression, naive bayes and decision trees.
* Training set will be split in to k fold, with each model being trained on `(k-1)` folds and using `kth` fold to predict. This process is repeated such that each model has used each fold of the training set for prediction(same as using `cross_val_predict`).
* Now we have 4 prediction results(because we used 4 different classifiers at layer1) and one target variable. This will be used as the training set (4 input features and 1 target variable) to the next layer.
* After we have created the training set for the next layer, each classifier in the layer1 will now be trained on the entire training set.
* Similar process will be repeated for layer2 classifiers to predict and using their predictions to create the input for the next layer. Layer2 also could contain multiple classifiers.

**NOTE**: Scikit-learn provides `StackingClassifier`.
> Note that `estimators_` are fitted on the full `X` while `final_estimator_`
is trained using cross-validated predictions of the base estimators using
`cross_val_predict`.

## Blending

* Here the training set will be split in to `n-1` hold out sets if we need n layers of blending. Each layer will use a hold out set for training.

* Suppose we want to have total 3 layers, a base layer with 2 layers of blending, then the training set will be split in to 3, a training set and 2 hold out sets.
* First part of the training set is used to train the base layer of classifiers.
* Then the base layer is given the first hold out set for prediction. The prediction results along with the target variable forms the training set for the next layer.
* After training the second layer, the remaining hold out set to passed through the first two layers for prediction and the predictions from the layer 2 on this hold out set along with the target variable will form the training set for the third layer(aka second layer of blending).

**NOTE**: In blending, each layer is trained on a subset of the actual training set.

## References

* [Ensemble learning](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-for-ensemble-models/)
* [Stacking using scikit-learn](https://www.mygreatlearning.com/blog/ensemble-learning/)
