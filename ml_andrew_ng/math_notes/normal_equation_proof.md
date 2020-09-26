# Proof of the normal equation

We want to find the parameters theta from the following equation.

```text
Y = X • theta

transpose(X)•Y = transpose(X)•X•theta

theta = inverse(transpose(X)•X) • transpose(X) • Y
```

The trick is to premultiply the first equation by transpose(X). Matrix inverse operation is only defined on square matrix. Premultiplying transpose(X) with the matrix X transforms the resultant matrix as a square matrix. Then only we can apply matrix inverse on transpose(X) • X.
