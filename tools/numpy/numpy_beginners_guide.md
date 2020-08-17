# Numpy guide for beginners

## Numpy vs Builtin Lists

* Numpy uses less memory to represent integers.
* Numpy uses contiguous memory locations to store data. Utilizes the SIMD(Single instruction multiple data) vector processing. More effective cache utilization.
* Lot more operations available compared to Lists.

## Basics

```Python
import numpy as np

# 1d array
a = np.array([1,2,3])

# 2d array
b = np.array([[1,2,3], [4,5,6]])
```

---

## References

* [The Ultimate Beginner’s Guide to NumPy](https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54)
* [Python NumPy Tutorial for Beginners](https://youtu.be/QUT1VHiLmmI)
* [Python NumPy Tutorial for Beginners repo](https://github.com/KeithGalli/NumPy)
