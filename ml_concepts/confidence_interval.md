# Standard error of the mean and Confidence interval

## Standard error of the mean (SEM)

SEM measures how precise the sample mean is an estimate of the population mean.

$$SEM = \sigma/\sqrt{N}$$

where $\sigma$ is the standard deviation and N is the sample size. $SEM <= SD$ always

From the above formula, **SEM decreases with increase in the sample size** (i.e) with increase in sample size, we get close to the population and hence the sample mean will be closer to the population mean.

## Confidence interval

- Sample refers to subset of observations from a population.
- Inference refers to drawing conclusions about the population from the sample.
- A sample can almost never represent a population perfectly giving rise to **sampling error**.
- An estimate of a population parameter is given as a confidence interval.
- Width of the confidence interval depends on variation of objects within the population and the sample size.
- If population has varied objects, sample measures will differ from each other, whereas if the population has similar objects, then sample measures will also be closer. So population with low variation leads to smaller confidence interval.
- Larger the sample size, more resemblance to population and hence lesser sampling error. Large sample size will also lead to narrow confidence interval.

## Bootstrapping a sample and confidence interval

- Suppose we want to compute the mean weight of all female mices, but we have a sample of 12 female mices.
- Bootstrapping refers to **sampling with replacement**. To create a bootstrapp sample of mices, we randomly pick 12 mices from the sample we have. Due to sampling with replacement we could have the same mice selected multiple times.
- For each of the new sample bootstrapped out of the sample we have, we calculate its mean.
- Repeating this bootstrapping process will yield us a new sample of mices. Thus we will have a bunch of different sample means.

- 95% confidence interval will cover 95% of the sample means.

---

## References

- [Standard error of the mean](https://www.investopedia.com/ask/answers/042415/what-difference-between-standard-error-means-and-standard-deviation.asp)
