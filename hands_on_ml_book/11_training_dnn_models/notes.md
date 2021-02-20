# 11. Training deep neural networks

Deep neural networks suffer from vanishing and exploding gradients problem.

## Vanishing gradients

* When we consider activation function like sigmoid function, the functions's range is [0, 1]. Also the sigmoid function is saturating, meaning larger negative or positive values of input causes the function to either move close to 0 or 1 respectively.

* So in backpropagation, we compute the gradients of error with respect to that connection. This gradient is computed using the chain rule, which means we would end up computing derivative of activation function with respect to the linear combination.
* If the activation function itself ranges from [0, 1], then the gradient will also be in that range.
* Also when the function is saturating, the gradients near those saturating values will also be really small in other words very close to 0.

```Python
# consider 10 layer network
# suppose 10th layer has gradient of activation function to be 0.5
# Every gradient of sigmoid activation function will be in range 0 and 1

from random import random, seed
seed(1)
acc = 1
for r in (random() for _ in range(10)):
    acc *= r

print(acc) # we get 6.75 * 10^-6
```

* Thus the nature of activation functions like sigmoid, tanh which are saturating and have a smaller range resulting in the gradients of lower layers in deep neural networks to be really small.
* When the gradient of lower layers are too small, gradient descent hardly updates the connection weights.
* This makes learning impossible/very slow in the lower layers. As a result higher layers too dont learn much and hence neural networks perform poorly.
* **Weight initialization along with sigmoid activation also contributed to vanishing gradients problem**. Commonly used weight initialization scheme was to use standard normal distribution with mean 0 and standard deviation of 1.

### 1. Fixing vanishing gradients using weight initialization

#### Glorot initialization

Weights should be initialized using the following formula

* Normal distribution, `variance = 1/fan_avg`, where `fan_avg = (fan_in + fan_out)/2`
* Uniform distribution, range `[-r, r]`, where `r = sqrt(3/fan_avg)`

Glorot initialization can speed up the training process considerably. This initialization works well with **sigmoid, tanh and softmax** activation functions.

#### LeCun Initialization

* Normal distribution, `variance = (1/fan_in)`

**NOTE**: LeCun = Glorot initialization with normal distribution,
when `fan_in = fan_out`

This initialization scheme is preferred for **SELU** activation function.

#### He Initialization

* Normal distribution, `variance = 2/fan_in`

This initialization scheme is preferred for **ReLU and its variants**. ReLU has the following variants

* Leaky ReLU
* Random ReLU
* Parameterized ReLU

#### Customizing initialization using keras

```Python
from tensorflow import keras
custom_he_initializer = keras.initializers.VarianceScaling(scale=2.0, mode="fan_avg", distribution="uniform")
```

### 2. Using non saturating functions

#### ReLU

* Its non saturating. But the gradient is 0 when the linear combination is less than 0.
* This leads to **dying neurons** problem. For all those neurons with linear combination < 0, the activation function outputs 0. Its equivalent to turning off that neuron.
* Also when we compute the gradients for those neurons, the gradient of ReLU is 0 when the input to ReLU activation is negative. This stops the weights update for those neurons.

**NOTE**: ReLU(x) is not differentiable at x=0.

#### Leaky ReLU

* To overcome the dying neuron problem, Leaky ReLU(z) = max(alpha*z, z)` where alpha=0.01. **alpha** is a hyperparameter of the leaky ReLU activation function.
* Here the gradient always exists. Hence there is no dying neuron.
* Leaky ReLU performs better than plain ReLU.

#### Randomized ReLU

* Here during training alpha is selected randomly within a given range.
* During predicting/testing, the alpha is fixed to the average value of the values in the input range.
* This activation function also seemed to act as a regulaizer.
* This performs better than leaky ReLU

#### Parameterized ReLU

* Here alpha becomes a model parameter that is updated by the back propagation process.
* Use this activation function only on large training sets.
* On smaller training data, this activation function causes overfitting.
* This outperforms previous variants of ReLU on larger training sets.

#### Exponential Linear Unit (ELU)

* This activation function also alleviates vanishing gradients problem
* This activation function outperforms all the variants of ReLU.
* But this is computationally expensive during training and testing.
* But this activation function causes the neural networks to converge faster in fewer epochs. So overall training time is reduced
* But when prediction has to be done with low latency, ELU activation function could prove to be computationally expensive.

```text
elu(z)  = alpha * [(e^z) - 1] when z < 0
        = z when z >= 0
```

#### SELU(Scaled ELU)

* Recommended for stack of dense layers.
* In such neural networks with dense layers, the network becomes self normalizing thus alleviating the vanishing gradients problem.
* This activation function outperforms all other activation functions significantly and is self normalizing

This activation function has the following preconditions to self-normalize

* Inputs should be standardized
* LeCun normal initialization for hidden layer weights.
* Sequential network architecture
* Hidden layers should be dense.

### 3. Using Batch normalization

* Can be applied either to the output of the linear combination or output of the activation function.
* Zero centers and normalizes input and then scales and shifts the normalized input.
* Basically, we learn the mean and the scale of the input during back propagation.

```text
# x is input vector
# x_norm is standardized input vector
x_norm = (x - mean)/std

# gamma scales and beta shifts the normalized x vector
batch_norm_out = gamma_vector .* x_norm + beta_vector
```

* During training, the mean and standard deviation of the mini batch is used for input standardization.
* But moving average of mean and standard deviation across all mini batches is also calculated. This value is used during the testing/prediction phase.

> Most implementations of Batch Normalization estimate these final statistics during training by using a moving average of the layer’s input means and standard deviations.

* Thus batch normalization contains gamma and beta vector which are trainable(updated by back propagation) and mean and standard deviation which are non trainable params(not updated by the back propagation)

* Authors of batch normalization technique recommend to use it before the activation function and after computing the linear combination.

* `momentum` and `axis` are some important Batch Normalization hyperparameters.
* `momentum` is used when updating the moving averages and `axis` determines which axis should be batch normalized.

#### Pros

* Fixed vanishing gradients problem even when saturating activation functions are used.
* Makes the network less sensitive to weights initialization.
* Acts as a regularizer.
* Faster convergence using larger learning rates.
* After training, we can fuse gamma and beta vector into weights and biases of previous layer. This will save us computation overhead during predictions.

#### Cons

* Training is slow. But it is compensated by much faster convergence(less epochs required)

## Exploding gradients

* Gradients can grow bigger and bigger and as a result weight updates are large leading to diverging from finding the solution.
* Exploding gradient problem occurs in recurrent neural networks.

### Fixing exploding gradient using gradient clipping

* Clip the gradients by either value or l2 norm during backpropagation.
* This technique is often used with Recurrent neural networks.

#### Gradient clip by value

* When `clipvalue=1.0` parameter is passed to optimizer like `SGD`, any gradient that's greater than 1 will be clipped to a value between `[-1, 1]`

* But clipping only few components of the gradient vector can change the direction of the gradient vector (gradient vector consists of gradients of loss to each input connection).

#### Gradient clip by norm

* This uses l2 norm of the gradient vector.
* When `clipnorm=5.0`, the gradient vector is rescaled such that the magnitude(l2) of rescaled vector is `<= 5.0`.
* This preserves the orientation of the vector(since its just a vector scaling operation).

## Using Pretrained layers (Transfer Learning)

* Find DNN models that are trained on similar task and use the lower layers of that model for training the problem we have.
* Reusing layers of pretrained models is known as **transfer learning**.
* For transfer learning to work well, we need to get the input size to the same as the one with which the original model was trained.
* Transfer learning works best with deep convolutional neural networks.

### Transfer learning pros

* Speeds up training compared to training from scratch.
* Models trained using transfer learning requires very less data.

### Transfer learning Cons

* Transfer learning does not work well when using layers from model with small dense networks. Works best for deep networks with lots of layers.

### How to select optimal number of layers for reuse

> Try freezing all the reused layers first (i.e., make their weights non-trainable so that Gradient Descent won’t modify them), then train your model and see how it performs. Then try unfreezing one or two of the top hidden layers to let backpropagation tweak them and see if performance improves. The more training data you have, the more layers you can unfreeze. It is also useful to reduce the learning rate when you unfreeze reused layers: this will avoid wrecking their fine-tuned weights.
> If you still cannot get good performance, and you have little training data, try dropping the top hidden layer(s) and freezing all the remaining hidden layers again. You can iterate until you find the right number of layers to reuse. If you have plenty of training data, you may try replacing the top hidden layers instead of dropping them, and even adding more hidden layers

## Unsupervised Pretraining

* Useful when the labelled data is very less.
* First we train the unlabelled data using autoencoder or GAN and then use lower layers of autoencoder or GAN's discriminator and add output layer on top and fine tune the final network using the labelled data.

## Pretraining on auxiliary task

* If we have supervised data for a similar problem or can prepare the supervised data very easily, but we dont have much labelled data for the problem that we are trying to solve, then we can create supervised data on the similar task and train a neural network
* Using the model trained on the similar task(auxiliary task), we can train for the actual problem in hand using transfer learning.

**NOTE** - Self-supervised learning is when we automatically generate labels from the data itself and training a model on the resulting labelled data.

## Faster Optimizers

### Momentum optimization

* Converges faster than plain gradient descent particularly on plateaus.
* Default Beta value(aka momentum hyperparameter) is 0.9

```Python
#theta is the weights vector
m = (Beta * m) - learning_rate * Gradient(J(theta))
theta = theta + m
```

When batch normalization is **not** used, upper layers of the neural network tend to have values are different scales. Using momemtum optimization helps a lot in such cases.

### Nesterov Accelerate Gradient

* aka Nesterov momentum optimization
* Converges faster than the plain momentum optimization.
* Compute the gradient with respect to (weights + Beta * m))

```Python
m = (Beta * m) - learning_rate * Gradient(J(theta + Beta * m))
theta = theta + m
```

### AdaGrad

* Adaptive gradient
* Here the gradient along the steepest dimension is scaled down.

```text
# s is a vector containing squares of each gradient
# since each gradient is squared, if the gradient is larger
# then its squared value will be larger compared to other gradients
s = s + Gradient(J(theta))^2
# epsilon is smoothing term and is set to 10^-10
theta =  theta - learning_rate * Gradient(J(theta)) / sqrt(s+epsilon)
```

* Each gradient's squared value is stored in `s` vector.
* Scale down each gradient by the square root of the corresponding component in the `s` vector. This is how the gradient with steep dimension is scaled down

* This algorithm uses **adaptive learning rate**. For steeper dimensions, the factor `Gradient(J(theta))/sqrt(s+epsilon)` will be smaller compared to other dimension's gradients. When this factor is multiplied by the learning rate, it decays the learning rate. Weight updates happen slower on the steeper dimension.

* When training neural networks `s` sometimes becomes too large, that the gradient updates become very small leading to very slow and early convergence before reaching the global optima.
* Hence adagrad is not used for training neural networks.

### RMSProp

* This optimizer also comes under adaptive learning rate algorithms.
* Very similar to adagrad. Here we dont accumulate squared gradients of all iterations.
* We introduce a decay rate to `s`.

```text
# s is a vector containing squares of each gradient
# since each gradient is squared, if the gradient is larger
# then its squared value will be larger compared to other gradients
# Beta is the decay rate
s = Beta * s + (1-Beta) * Gradient(J(theta))^2

# epsilon is smoothing term and is set to 10^-10
theta =  theta - learning_rate * Gradient(J(theta)) / sqrt(s+epsilon)
```

### Adam and Nadam optimizer

* Adam - Adaptive Moment Estimation - combines momentum with RMSProp.
* Nadam - Adam with nesterov optimizatio applied. So it will converge faster than Adam.
* Adamax - This uses `s = max(Beta *s, Gradient(J(theta)))` instead of the squared gradients.

## Learning rate scheduling

* Instead of going with constant learning rate, we could use learning schedules to update the learning rate automatically as the epochs increases.

* Exponential, performance and 1cycle scheduling can speed up convergence.

### Power scheduling

* t - current epoch number
* s - Number of epochs
* c - usually set to 1

```python
# learning rate as a function of iteration/epoch number
lr = init_lr / (1 + t/s) ** c
```

* When number of epochs keep increasing by `s`, learning rate is reduced by a factor of 2,3,4 etc.

* In this schedule, initially the learning rate drops quickly but then starts to drop slowly.

### Exponential scheduling

* As we complete `s` epochs, learning rate keeps getting dropped by a factor of 10.

```Python
lr = init_lr * (0.1) ** (t/s)
```

### Piecewise constant scheduling

* For every epoch range, we end up using different learning rates. Within that epoch range, the learning rate is fixed.

* Finding the right learning rate for each range of epochs is a bit tricky.

### Performance scheduling

* If the validation loss fails to decrease over a fixed number of epochs, then we can reduce the learning rate by a factor of **lambda**.

### 1Cycle scheduling

* Here we first increase the learning rate linearly from x to y halfway through the training
* In the next half of the training, we decrease the learning rate linearly from y back to x.
* Upper cap(y) for the learning rate is usually chosen to be 10 times that of the lower cap(x).
* To rightly choose the upper cap(y) we can use the technique discussed in tuining the learning rate hyperparameter in the previous chapter.

* If we are using the optimizer with momentum, then we start with high momentum and reduce the momentum linearly during first half. In the second half of the training, we start with this reduced momentum and increase linearly back to the original momentum with which we started.

## Regularization

* Any technique that avoid overfitting can be considered as a regularization technique.
* Early stopping is a regularization technique

### L1 and L2 regularization

* Use for L1 regularization when we need a sparse model.
* In neural networks, regularization is configured for each layer.

### Dropout

> It is a fairly simple algorithm: at every training step, every neuron (including the input neurons, but always excluding the output neurons) has a probability `p` of being temporarily “dropped out,” meaning it will be entirely ignored during this training step, but it may be active during the next step. The hyperparameter `p` is called the dropout rate, and it is typically set between 10% and 50%: closer to 20–30% in recurrent neural nets, and closer to 40–50% in convolutional neural networks. After training, neurons don’t get dropped anymore.

* Dropout creates a neural network of unique neuron combinations every step.
* Dropout is applied to upper layers in practice.

> Moreover, many state-of-the-art architectures only use dropout after the
last hidden layer, so you may want to try this if full dropout is too strong.

**NOTE**: * After training, all the input connection weights should be multiplied by (1-p). This is taken care in libraries like keras. But when we implement our own dropout, we need to ensure this.

* In case of self normalizing networks, we have to use **alpha dropout** so as to preserve the normalization.
* Always evaluate the trained model on the training set with dropout disabled to identify overfitting.
* Increasing the dropout rate(`p`) increases the regularization which helps to reduce overfitting.
* Dropout slows down convergence.

### Monte Carlo(MC) Dropout

* Averaging over multiple predictions made on the same dataset using dropout enabled gives the MonteCarlo estimate.
* Number of predictions to make is a hyperparameter. Higher its value, better the predictions and its uncertainty estimates. But high value also increases the prediction latency.

### Max norm regularization

* This is considered as a constraint.
* For each neuron, it constrains the weights such that `magnitude(w) <= r`.
* Here l2 norm of the vector is used and `r` is the hyperparameter.
* Reducing `r` increases the amount of regularization.
* This can be used to alleviate unstable gradients when batch normalization is not used.
