# Feature Hashing

* First we configure what should be the resulting vector dimension `N`
* Every value of the feature is given to a hash function and its hash is computed.
* Then we divide the hash value using `N` and the remainder is used as index to the result vector.
* We then add or subtract a constant at the vector (using the computed index).

> It has been suggested that a second, single-bit output hash function `ξ` be used to determine the sign of the update value, to counter the effect of hash collisions. - [Wikipedia: Feature Hashing](https://en.wikipedia.org/wiki/Feature_hashing)

```Python
 def feature_hashing(features, N : integer):
     x = [0] * N
     for f in features:
         h := hash(f)
         idx = h mod N
         if epsilon(f) == 1:
             x[idx] += 1
         else:
             x[idx] -= 1
     return x
```

* In scikit-learn, feature hashing is available as `sklearn.feature_extraction.FeatureHasher`

---

## References

* [Feature Hashing](https://en.wikipedia.org/wiki/Feature_hashing)
