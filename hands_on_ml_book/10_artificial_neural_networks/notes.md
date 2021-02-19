# 10. Introduction to ANN

## Biological neurons

* Each biological neuron receives its input via **dendrites**.
* Neuron contains a nucleus and a long tail called axon. At the end of the axon, we have **telodendria** which are a bunch of brances. At the tip of each branch we have synaptic terminals.
* We can think of these synaptic terminals as connection to other neurons.
* Once a neuron is activated, it releases electrical impulse called as Action Potential that travels through the axon and when it reaches the synaptic terminals, the electrical impulse produces chemical signals known as **neurotransmitters**.
* When a neuron receives a sufficient amount of neurotransmitters within a given time, that neuron is activated.

## Logical computation with neurons

* Each artificial neuron can have one or more binary inputs and 1 binary output.
* An artificial neuron is activated when certain amount of its inputs become active.
* With this simple architecture, we would be able to compute any logical propositions like **AND**, **OR**, **NOT** etc.

## Perceptron

* Perceptron acrhitecture is made up of **Threshold Logic Units(TLU)**.
* Each TLU contains many inputs that are numbers and outputs a number.
* Each connection from the TLU to the input is given a weight.
* The weighted sum(linear combination of weights and inputs) of the inputs is then fed to activation function associated with the TLU.
* This activation function is either a **heaviside or sign function**
* Perceptron is made up of single layer of TLUs. Number of TLUs in that single layer is determined by the problem output. Each TLU is connected to all the inputs.
* Simply put, we can consider Perceptron as containing a layer of input neurons and a layer of output neurons. The output layer neurons are TLUs.
* Sometimes a **bias neuron** can also be added to the input layer of neurons.
* For instance, in a binary classification problem, the perceptron will contain a single TLU. In a multiclass classification problem, we would have 1 TLU for each class.

**NOTE**: When current layer is fully connected to the previous layer, it is called as fully connected layer or dense layer.

### Perceptron learning rule

* This rule reinforces the connections that help reduce the error.
* Below formula performs a gradient descent step.

```text
# Gradient computes the partial derivative of how much
# this input neuron connection contributed to the error which is 
# computed by the cost function.
# dC/dw = dC/dz * dz/dw
gradient = (y - yhat) * input value of ith neuron

Weight of ith input neuron connected to jth output neuron = current weight +
 learning_rate * gradient
```

### Limitations

* Perceptron is suitable only for training instances that are linearly separable(since decision is made depending on `Z > threshold`). Its not suitable for learning complex patterns.
* Perceptron convergence theorem - If the training instances are linearly separable, then perceptron algorithm will converge to a solution.
* Perceptron are capable only of hard classification(soft classification means output probabilities)

## MultiLayer Perceptron

* In this multilayer perceptron architecture, we have first layer which is the input layer and then a number of subsequent layers called as the hidden layers and the last layer which is the output layer.
* A bias neuron can be added to all the layers starting from the first hidden layer.
* Hidden layers closer to the output layer are referred to as upper layers and the hidden layers closer to the input layer is referred to as lower layers.
* Lower layers usually learn low level features and upper layers learn high level features.
* Thus as we move up the layers, the learning becomes more relevant to the problem that we are solving.
* When the signal flows in the direction starting from the input to the output layer, the such networks are called as **feedforward neural networks**.
* When the number of hidden layers are large, then the neural networks are referred to as **deep neural networks** and the field is referred to as **deep learning**

### Backpropagation training algorithm

* Neural network is fed a training instance(or a mini batch of training instances) for learning.
* Learning is a forward pass. Input signal move from input layer to the output layer. Once we get the output from the final layer, we compute the error using the cost function.
* Now in the backward pass, we try to propagate how much each connection contributed to the error and adjust the connection weights accordingly.
* Hence the name of this algorithm is back propagation.
* In the backward pass, we compute the gradient of the error with respect to each connection weight using the **chain rule**.
* Once all the gradients are computed, a gradiant descent step should be performed.
* Thus for the back propagation to work, **we need to have cost function as well as the activation functions that are differentiable**.
* Also for the neural networks to learn properly, the weights of the connections have to be initialized randomly. This causes each neuron to learn different features from the input (**breaking symmetry**).
* If all weights are initialized to zero, then all the neurons learn the same thing and each connection would contribute the same amount to the error.

### Activation function

* In original perceptron architecture, we used heaviside or sign function as the activation function. But the gradient descent step cannot be performed on those functions.
* In MLP, the activation function was changed to using **sigmoid function**(aka logistic function used in the logistic regression).
* We also have other activation functions like **tanh**, **relu**, **softplus**

```text
#z is the linear combination of inputs and weights
sigmoid = 1 / ( 1 + e^-z )

tanh = 2 * sigmoid(2 * z) - 1

relu = max(0, z)

softplus = log( 1 + e^ )
```

**NOTE**: These activation functions introduce non linearity between layers. This provides the neural network to approximate any continuous function.

## Regression MLP

* Output neurons - Number of features to predict
* Hidden layer activations - Relu or its variants
* Output layer activation - None, relu/softplus(positive output), sigmoid or tanh(output within a range [0, r] and [-r, r] respectively)
* Loss function - MSE, MAE, Huber loss

MSE - sensitive to outliers
MAE - less sensitive to outliers
Huber is quadratic till a threshold. After the threshold, its linear

## Classification MLP

* Output neurons - Depending on the problem type(binary - 1, multiclass-n, multioutput, multilabel - 1 per label)
* Hidden layer activations - Relu or its variants
* Output layer activation - sigmoid, softmax(multiclass)
* Loss function - Cross entropy

## Fine tuning neural network hyperparameters

To find good hyperparameters, we could use grid search or random search from scikit-learn or we could use other hyperparameter optimization libraries like **Hyperopt, Hyperas etc**

### Number of hidden layers

* Real world data has hierarchial structure. So multiple hidden layers can be used to learn features from the data's hierarchy.
* We could also reuse lower layers of a model trained on a similar task to our problem(transfer learning)
* Complex problems like image classification, speech recognition require deep neural network.

### Number of neurons per hidden layer

* Number of neurons in each hidden layer forming a pyramid structure(many low level features and few higher level features). But this practice has largely been abandoned.
* Stretch pants approach - Take more hidden layers and lots of neuron per layer and use regularization and early stopping to avoid overfitting.

### Learning rate

* We could use some learning schedule that updates the learning rate every epoch(iteration).
* Then we would plot loss and learning rate(log scale). We could pick the learning rate at which the loss starts to increase. We then reduce that selected learning rate by some amount(typically l10 times lower) and use that learning rate to train the neural network from scratch.
* But there are also other techniques that work well with learning rate varying over epochs like power scheduling, exponential scheculing, cycle scheduling etc.

### Optimizer

* Choosing a good optimizer helps the neural network converge faster to a good solution.

### Batch size

* Either use small batch sizes like 32
* If you are using larger batch sizes, then use learning rate warmup so that the training generalizes well. If training is unstable, then we could switch to using smaller batch sizes.

### Activation Function

* Relu is a good default. But there are other variants of RELU that we could try for hidden layers.

### Number of epochs

* We could use large number of epochs and use early stopping.

---

## Additional references

* [Training stability](https://machinelearningmastery.com/how-to-control-the-speed-and-stability-of-training-neural-networks-with-gradient-descent-batch-size/)
* [Challenges when using large batch sizes](https://infohub.delltechnologies.com/p/challenges-of-large-batch-training-of-deep-learning-models/)
* [A disciplined approach to neural network hyper-parameters: Part 1 -- learning rate, batch size, momentum, and weight decay](https://arxiv.org/abs/1803.09820)
