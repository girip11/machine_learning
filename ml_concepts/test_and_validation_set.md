# Test set and validation set

> – **Training set**: A set of examples used for learning, that is to fit the parameters of the classifier.
> – **Validation set**: A set of examples used to tune the parameters of a classifier, for example to choose the number of hidden units in a neural network.
> – **Test set**: A set of examples used only to assess the performance of a fully-specified classifier.
> — Brian Ripley, page 354, Pattern Recognition and Neural Networks, 1996

Total dataset is split into

* Training set and
* Test set

If we have several different models, we train all these different models on the training set and evaluate the model performance on the test set.

But if we have selected a model among many different models and wanted to tune the hyperparameters of the selected model, then we will divide the training dataset further into

* Training set for model development with different hyperparameter values (train dev set)
* Validation set

All models that were trained on **train dev set** will be evaluated on the validation set to select the model with optimal performing hyperparameters.

Once the model is finalized with its hyperparameter values for that application, the model is trained on the original entire training set and evaluated on the test set.

## K-fold cross validation

Instead of using a separate validation dataset, the better approach is to use k-fold cross validation to tune the model hyperparameters.

> Reference to a “validation dataset” disappears if the practitioner is choosing to tune model hyperparameters using k-fold cross-validation with the training dataset. - Jason Brownlee

---

## References

* [Test set and validation set](https://machinelearningmastery.com/difference-test-validation-datasets/)
