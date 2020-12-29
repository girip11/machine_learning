# Feature selection

Feature selection methods can be categorized in to

* Filter methods
* Wrapper methods
* Embedded methods

## Filter methods

* Filter methods are model agnostic. They use statistical methods to determine how the feature is correlated to the target variable.

  * Basic methods
  * Univariate feature selection
  * Information gain
  * Fischer score
  * ANOVA F-Value for Feature Selection
  * Correlation Matrix with Heatmap

### 1. Basic methods

* Remove columns with constant value for all the rows.
* **Quasi-constant features** are those that show the same value for the great majority of the observations of the dataset.
* Remove the columns with lesser variance(they have very few unique values compared to the training dataset size). `VarianceThreshold` from sklearn can be used to remove such features.

### 2. Univariate selection methods

* Univariate feature selection methods works by selecting the best features based on univariate statistical tests like **ANOVA**.

* Methods based on f-test assume linear relationship between the feature and the target.

* There are statistical methods to estimate the linear as well as the non linear dependency between the feature and the target variable.

* scikit-learn provides methods like `SelectKBest`, `SelectPercentile` etc from `sklearn.feature_selection` module.
* Both the above classes accept a scoring function.
  * For regression tasks: `f_regression`, `mutual_info_regression`
  * For classification tasks: `chi2`, `f_classif`, `mutual_info_classif`

> The methods based on F-test estimate the degree of linear dependency between two random variables. On the other hand, mutual information methods can capture any kind of statistical dependency, but being nonparametric, they require more samples for accurate estimation.
> **NOTE**: Beware not to use a regression scoring function with a classification problem, you will get useless results.

 **NOTE**: `chi2` works for features with non negative values only and that too only for discrete target(classification problems).

#### Information gain (aka mutual information)

> Mutual information measures the information that X and Y share: It measures how much knowing one of these variables reduces uncertainty about the other. For example, if X and Y are independent, then knowing X does not give any information about Y and vice versa, so their mutual information is zero. At the other extreme, if X is a deterministic function of Y and Y is a deterministic function of X then all information conveyed by X is shared with Y: knowing X determines the value of Y and vice versa. As a result, in this case the mutual information is the same as the uncertainty contained in Y (or X) alone, namely the entropy of Y (or X). Moreover, this mutual information is the same as the entropy of X and as the entropy of Y. (A very special case of this is when X and Y are the same random variable.) - **Wikipedia**

* `mutual_info_classif` and `mutual_info_regression` are available in `sklearn.feature_selection` module. These functions are based on non parametric methods based on entropy estimation.

#### Fisher score (`chi2`)

* It computes **chi-squared stats** between each **non-negative** feature and class.
* This is often used to find the **importance of a categorical feature** against a categorical task(classification task).

#### ANOVA F-value for feature selection

* `sklearn.feature_selection.f_classif` computes ANOVA F-value for the input **numerical value** againt the categorical target variable(classification task).

### 3. Correlation Matrix with heatmap

* Correlation coefficient (Pearson correlation) between two variables measures the linear relationship between those 2 variables.

* Correlation coefficient takes values in the range [-1, 1], with -1 for strong negative correlation while 1 stands for strong positive correlation and 0 means no correlation.

* Using the correlation matrix `pandas.DataFrame.corr`, we can determine features that are correlated with each other. Using this information we can retain only one of the correlated feature and remove the other.

---

## References

* [Mutual Information](https://en.wikipedia.org/wiki/Mutual_information)
* [Comprehensive Guide on Feature Selection](https://www.kaggle.com/prashant111/comprehensive-guide-on-feature-selection)
* [Feature selection course on udemy](https://www.udemy.com/course/feature-selection-for-machine-learning/)
