# Information theory required for machine learning

* Information theory deals with quantifying information for communication.

## Information

* Events that have low probability(surprising) of occuring will carry more information compared to events with high probability(unsurprising).
* Amount of information aka **Shannon information** associated with an event is given by `h(x) = -log(p(x))`, where `p(x)` is the probability of event x and the `log` is a base-2 logarithm because we are measuring information interms of bits.
* We know `log(0)` is `-inf` and `log(1)` is equal to 0. Probability can take values in the range `[0, 1]`. So the negative sign used in the `h(x)` will ensure the result will always be `>= 0`

```Python
from math import log
# base is 2
log(0.01, 2)

log(0.99, 2)

log(1.0, 2)
```

> Information will be zero when the probability of an event is 1.0 or a certainty, e.g. there is no surprise.

* Lesser the probability of an event, more will be the number of bits required to encode it.

## Entropy for a random variable

* Information for a random variable is the same as computing information for every value that the random variable will take.

* Calculating information for a random variable is known as **information entropy** or **shannon entropy**.

* Suppose X is a discrete random variable that can take values 1,2,..n. Then the information for the random variable X is given by `H(X) = -sum(p(x) * log(p(x), 2) for x in X)`

> The intuition for entropy is that it is the average number of bits required to represent or transmit an event drawn from the probability distribution for the random variable.

* Entropy of a random variable is lowest if its random variable with 1 certain event(`p(x)=1`) and other events are uncertain(`p(x)=0`)(think of one hot encoding). Entropy for a random variable will be the highest, if the random variable probability distribution is [uniform](https://en.wikipedia.org/wiki/Discrete_uniform_distribution).

```Python
from scipy.stats import entropy

# probabilities of values on rolling a die
probabilities = [1/6] * 6

entropy(probabilities, base=2)
```

* Skewed probability distributions have less surprises and hence less entropy while uniform probability distributions have high entropy.

**NOTE**: Entropy for a distribution like `[1, 0, 0, 0]` is 0.0.

## Cross entropy

> Cross-entropy is a measure of the difference between two probability distributions for a given random variable or set of events.

* In machine learning, for instance in a classification problem, the target variable for a particular instance will have a probability distribution for its classes like `[1, 0, 0, 0]`(when classes are mutually exclusive, think of multiclass classification). Once the model learns about the instance and predicts the probabilities for the target classes `[0.8, 0.05, 0.1, 0.05]` which would form another probability distribution Q. Q can be thought of as an approximation of the distribution P.

> The intuition for this definition comes if we consider a target or underlying probability distribution P and an approximation of the target distribution Q, then the **cross-entropy of Q from P is the number of additional bits to represent an event using Q instead of P**.
> `H(P, Q) = -sum(P(x) * log2(Q(x)) for x in X)`

* If Q and P are very different distributions(think wrong probabilities for target classes), then we will need more bits to represent P using Q. But if Q is as close as P then the number of additional bits required would be that of P only.

* Cross entropy is different from KL divergence. Cross entropy measures the total number of bits required to represent an event from P using Q, while KL divergence measures the average number of bits required. Formula for computing KL divergence is `KL(P || Q) = – sum x in X P(x) * log(Q(x) / P(x))`

* `H(P, Q) = H(P) + KL(P || Q)`(using log's quotient rule and simplifying)

* From the formula for computing cross entropy, we can observe that the cross entropy is **not symmetrical**.

> If two probability distributions are the same, then the cross-entropy between them will be the entropy of the distribution.

* Cross entropy is often used as loss function for solving classification problems using logistic regression, artificial neural networks.

> We can see a super-linear relationship where the more the predicted probability distribution diverges from the target, the larger the increase in cross-entropy.

* **Log loss** and cross entropy calculate the same thing when used as loss functions. For classification problems, “log loss“, “cross-entropy” and “negative log-likelihood” are used interchangeably.

### Log loss and Maximum likelihood

## Information Gain

* Information gain measures the reduction in entropy by splitting a dataset for a given value of a random variable.
* Entropy of a dataset is its probability distribution of random variable(target categorical variable which is a discrete for classification tasks).

> A dataset with a 50/50 split of samples for the two classes would have a maximum entropy (maximum surprise) of 1 bit, whereas an imbalanced dataset with a split of 10/90 would have a smaller entropy as there would be less surprise for a randomly drawn example from the dataset.
> In this way, entropy can be used as a calculation of the purity of a dataset, e.g. how balanced the distribution of classes happens to be.
> Information gain provides a way to use entropy to calculate how a change to the dataset impacts the purity of the dataset, e.g. the distribution of classes. A smaller entropy suggests more purity or less surprise.

* In machine learning dataset, each feature can be thought of as a random variable that can be used to split the dataset and this split would affect the dataset's purity/distribution of target classes.

* Information gain on a dataset S when split using a random variable with value a is given by `IG(S,a) = H(S) - H(S|a=v)`. `H(S)` - Entropy before the split and `H(S|a=v)` refers to the conditional entropy of the dataset given the random variable `a=v`(it refers to a feature in machine learning terms).

* When we split the dataset S at feature `a=v`, we split the dataset S in to 2 groups S1 and S2. Conditional entropy is given by `H(S|a = v) = len(S1)/len(S) * Entropy(S1) + len(S2)/len(S) * Entropy(S2)`

* Suppose the feature/random variable `a` takes 10 values. Then for each value that `a` can take, we compute the information gain IG so that the one `a=v` with the maximum gain will lead to purest splitting of the dataset S. This is what is used in the decision trees( calculate the information gain between the target variable and each input variable in the training dataset).

> Note that minimizing the entropy is equivalent to maximizing the information gain.

## Mutual Information

> A quantity called mutual information measures the amount of information one can obtain from one random variable given another.

* Mutual information between two random variables X and Y is given by `I(X given Y) = H(X) - H(X|Y)`

* Mutual information is symmetrical `I(X; Y) = I(Y; X)`

* X alone would have some entropy(surprises/uncertainity). Mutual information measures the reduction in entropy(uncertainity) of X given the knowledge of Y.

> * Mutual information can be calculated as the KL divergence between the joint probability distribution and the product of the marginal probabilities for each variable. `I(X; Y) = KL(p(X, Y) || p(X) * p(Y))`
> * Mutual information is always larger than or equal to zero, where the larger the value, the greater the relationship between the two variables. If the calculated result is zero, then the variables are independent.
> * Mutual information is often used as a general form of a correlation coefficient, e.g. a measure of the dependence between random variables.

---

## References

* [Entropy in information theory](https://machinelearningmastery.com/what-is-information-entropy/)
* [Information Gain and Mutual Information for Machine Learning](https://machinelearningmastery.com/information-gain-and-mutual-information/)
* [A Gentle Introduction to Maximum Likelihood Estimation for Machine Learning](https://machinelearningmastery.com/what-is-maximum-likelihood-estimation-in-machine-learning/)
* [A Gentle Introduction to Cross-Entropy for Machine Learning](https://machinelearningmastery.com/cross-entropy-for-machine-learning/)
