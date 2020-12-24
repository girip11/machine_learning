# Hyperparameter tuning

## Methods

* Random Search - We provide a set of values of each hyperparameter as part of the parameter grid. In each iteration random search selects a random combination of these hyperparameters and trains the model. Parameters with the best performance will be returned at the end of n iterations.

* Grid Search - Runs all the combinations of all the hyperparameter values provided in the parameter grid.

* Bayesian Optimization
* Tree-structured Parzen Estimators (TPE)

## Algorithms

* [Hyperband](https://arxiv.org/abs/1603.06560)
* [Population based trainig (PBT)](https://deepmind.com/blog/article/population-based-training-neural-networks)
* [Bayesian Optimization and HyperBand(BOHB)](https://www.automl.org/blog_bohb/)

## Libraries

These libraries support tuning scikit-learn models.

* Raytune (very powerful, distributed hyperparameter sweep, Hyperband, PBT, Bayesian Opt)
* Optuna (light weight)
* mlmachine (bayesian opt on multiple estimators)
* Scikit-Optimize
* HyperOpt (TPE)
* BayesianOptimization and
* GPyOpt

---

## References

* [Hyperparameter Tuning](https://neptune.ai/blog/hyperparameter-tuning-in-python-a-complete-guide-2020)
* [Hyperparameter optimization frameworks](https://towardsdatascience.com/10-hyperparameter-optimization-frameworks-8bc87bc8b7e3)
* [Hyper-Parameter Tuning Techniques](https://medium.com/swlh/4-hyper-parameter-tuning-techniques-924cb188d199)
* [Bayesian Optimization](https://thuijskens.github.io/2016/12/29/bayesian-optimisation/)
