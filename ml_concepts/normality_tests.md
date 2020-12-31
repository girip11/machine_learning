# Normality assumption

## What is the need for normality tests?

> Parametric statistical methods assume that the data has a known and specific distribution, often a Gaussian distribution. If a data sample is not Gaussian, then the assumptions of parametric statistical tests are violated and nonparametric statistical methods must be used.

```text
If Data Is Gaussian:
    Use Parametric Statistical Methods
Else:
    Use Nonparametric Statistical Methods
```

## Testing for normality assumption visually

* Histogram. But with fewer samples histogram might not be the suitable plot.
* Density plots(smoothened version of histogram). With fewer samples, it might be hard to visually detect if the features normal distribution.
* **Quantile-Quantile plot**(QQ-plot) is a better way to evaluate the normality assumption and these plots are independent of the sample size.

* A very good notebook on qqplots can be found [here](http://www.cse.chalmers.se/~richajo/dit862/L4/Lecture%204%20(Q-Q%20plots).html)

> With QQ-plots we only need to ascertain whether the data points follow the line (sometimes referred as Henry’s line).
> If points are close to the reference line and within the confidence bands, the normality assumption can be considered as met. The bigger the deviation between the points and the reference line and the more they lie outside the confidence bands, the less likely that the normality condition is met.
> When facing a non-normal distribution as shown by the QQ-plot, the first step is usually to apply the logarithm transformation on the data and recheck to see whether the log-transformed data are normally distributed.

## Statistical methods

* Shapiro-Wilk's test (`scipy.stats.shapiro`) - This test has a drawback when we have duplicate values. Recommended when there are thousand or fewer observations.
* D'Agostino and Pearson. (`scipy.stats.normaltest`)- Recommended
* Anderson-Darling Test (`scipy.stats.anderson`)
* Kolmogorov-Smirnov test (`scipy.stats.kstest`)

### How statistical tests work?

Null hypothesis(H0): Data follow a normal distribution
Alternate Hypothesis: Data do not follow a normal distribution

A threshold level is chosen called alpha, typically 5% (or 0.05), that is used to interpret the p-value. You can interpret the p value as follows.

* p <= alpha: reject H0, not normal.
* p > alpha: fail to reject H0, normal.

The p-value is not the probability of the data fitting a Gaussian distribution

> A normality test is a hypothesis test, so as the sample size increases, their capacity of detecting smaller differences increases. So as the number of observations increases, the Shapiro-Wilk test becomes very sensitive even to a small deviation from normality. As a consequence, it happens that according to the normality test the data do not follow a normal distribution although the departures from the normal distribution are negligible and the data in fact follow a normal distribution.

**NOTE** - Recommended way is to use QQ-plot with either **D'Agostino** or **Shapiro** tests.

## Conclusion

* Hard fail - When any of the methods fail to satisfy the normality assumption
* Soft fail - when some method fail, then assume that the distribution is gaussian like and proceed with the parametric statistical methods.

---

## References

* [A Gentle Introduction to Normality Tests in Python](https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/)
* [Normality ipython notebook](https://github.com/robertdefilippi/normality-applications-python)
* [Testing for Normality — Applications with Python](https://medium.com/@rrfd/testing-for-normality-applications-with-python-6bf06ed646a9)
* [Normality tests](https://towardsdatascience.com/do-my-data-follow-a-normal-distribution-fb411ae7d832)
