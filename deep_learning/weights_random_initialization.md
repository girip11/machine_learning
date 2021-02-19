# Why weights should be initialized randomly?

## Initialize all weights to 0 or constant

* Suppose we initialize all the weights to 0, linear combination (aka pre-activation) becomes 0 for all neurons. So any activation function will output the same value. So output from all the neurons of the first hidden layer will be identical(basically the value of activation function at 0)
* From there onwards, all neurons in each layer will output the same value since the weights of the entire network is initialized to 0 (every neuron will see the same inputs and the same weights).
* Also during the back propagation, the gradient will be same for each neuron and each connection weight will be updated by the same amount.
* Every neuron in the network will look identical and will mostly likely converge to a suboptimal solution.
* This is referred to as symmetry of neural network. By initializing the weights of each neurons randomly, [we break this symmetry](https://stackoverflow.com/questions/59638646/what-does-it-mean-to-break-symmetry-in-the-context-of-neural-network-programm) and each weight will have a different gradient and hence a different weight update every iteration.
* This could help the network to converge to a global optima.

---

## References

* [Why Initialize a Neural Network with Random Weights?](https://machinelearningmastery.com/why-initialize-a-neural-network-with-random-weights/)
