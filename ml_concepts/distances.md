# Distance measures in Machine learning

## Hamming distance

- Used to find the number of bits that are different between two bitstrings(binary strings).

> For bitstrings that may have many 1 bits, it is more common to calculate the **average number of bit differences** to give a hamming distance score between 0 (identical) and 1 (all different).

$$\sum_{i=0}^{N} |X_{i} - Y_{i}| / N$$

where `X` and `Y` are two bitstrings.

- Scipy library implementation under `scipy.spatial.distance.hamming`

## Euclidean distance

- Related to **L2 vector norm**.
- Used to measure the distance between 2 real valued vectors.
- Often the **vector components are normalized or standardized** before applying the euclidean distance so that the scale is same. Otherwise larger component will shadow smaller components.
- Most instance based machine learning algorithms use euclidean distance.

$$\sqrt{\sum_{i=0}^{N} (X_{i}-Y_{i})^{2}}$$

- Scipy implementation - `scipy.spatial.distance.euclidean`

- This is used as a cost function or for measuring performance in the form of mean squared error or root mean squared error.

- MSE is used when the operation is to be repeated large number of times.(saving the expensive `sqrt` computation time)

## Manhattan distance or Taxicab or cityblock distance

- Related to L1 vector norm.
- Not sensitive to outliers.

$$\sum_{i=0}^{N} |X_{i}-Y_{i}|$$

- When divided by the total vector components, we get **mean absolute error**.
- Scipy implementation - `scipy.spatial.distance.cityblock`

## Minkowski distance

- used for calculating distance between any two real valued vectors.
- Its a generalization over euclidean and manhattan distance.

$$\sqrt[p]{\sum_{i=0}^{N} |X_{i}- Y_{i}|^{p}}$$

## Vector max norm

- Returns maximum absolute value in a vector
- Denoted as $||V||_{\inf}$ and calculated as $max(|V_{0}|,...,|V_{n}|)$

```Python
from numpy import inf
from numpy import array
from numpy.linalg import norm
a = array([1, 2, -3])
print(a)
maxnorm = norm(a, inf)
print(maxnorm) # prints 3.0
```

- Used as a regularization technique in neural networks.

## References

- [Distance measures in Machine learning](https://machinelearningmastery.com/distance-measures-for-machine-learning/)
- [Vector norms](https://machinelearningmastery.com/vector-norms-machine-learning/)
