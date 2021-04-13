# 14. Deep Computer Vision Using Convolutional Neural Networks

* CNNs are used in computer vision, speech recognition etc.
* CNNs are inspired from the way human visual cortex work.

## Architecture of the Visual Cortex

* Neurons in the visual cortex don't see the entire visual field, rather a subsection of it termed as **local receptive field**. These receptive fields of different neurons can overlap.
* Lower level neurons see primitive low level features and higher level neurons starting seeing complex features.

## Why CNN?

* Larger images have more pixels and hence more input features. Fully connected feed forward neural networks don't perform well on such larger images.

### Convolutional layer

* Neurons in a convolutional layer are not fully connected to the inputs from the previous layer, rather they are connected only to the inputs that fit into its receptive field.

* Size of the receptive field is a hyperparameter.

* Multiple CNN layers stacked on top of each other creates a hierarchy that help learn low level features to complex high level features.

* Inputs of CNN is represented in 2D. This means neurons in the hidden layers will also be arranged into a matrix.

> A neuron located in row `i`, column `j` of a given layer is connected to the outputs of the neurons in the previous layer located in rows `i to i + fh – 1`, columns `j to j + fw – 1`, where fh and fw are the height and width of the receptive field.

* **Zero padding** is done around the inputs(all 4 sides of the input matrix) to match the receptive field size of the neurons in the next layer(Receptive fields of neurons in the boundaries tend to see beyond the boundaries of inputs in the previous layer if the previous layer has the same size as the next layer).

* Receptive fields are spaced out(no sidewise overlap) when we need to connect a large input layer to next layer that's small. **stride** is the hyperparameter that refers to the amount by which we need to shift from one receptive field to the other. Two neighbouring neurons in a layer will have their receptive fields set apart by **stride units**.

* We can configure vertical as well as horizontal stride length.

> A neuron located in row `i`, column `j` in the upper layer is connected to the outputs of the neurons in the previous layer located in rows `i × sh` to `i × sh + fh – 1`, columns `j × sw` to `j × sw + fw – 1`, where `sh`
and `sw` are the vertical and horizontal strides.

```Python
# compute the final size of input layer given the size
# of next layer, receptive field length, and stride length
from typing import Tuple

def compute_input_size(
    next_layer_size: Tuple[int, int],
    receptive_field_width: int,
    receptive_field_height: int,
    stride_width: int,
    stride_height: int) -> Tuple[int, int]:
    last_item_row = next_layer_size[0] - 1
    last_item_col = next_layer_size[1] - 1

    # last input seen by the last neuron will tell us
    # how much the input layer size needs to be
    last_input_row = (last_item_row * stride_height) + receptive_field_height - 1
    last_input_col = (last_item_col * stride_width) + receptive_field_width - 1

    return last_input_row + 1, last_input_col + 1

input_size = compute_input_size((3, 4), 3, 3, 2, 2)
print(input_size)
# for (3,4) layer, we need input size of 7,9 with the given
# receptive field and stride sizes.
```

### Filters
