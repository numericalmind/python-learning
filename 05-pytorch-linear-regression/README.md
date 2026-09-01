# PyTorch Linear Regression

A simple linear regression project built with PyTorch to understand the fundamental training workflow of a neural network.

This project is part of my learning path toward **Physics-Informed Neural Networks (PINNs)** and scientific machine learning.

## Objective

The goal is to train a simple linear model to learn the relationship:

$$
y = 2x + 1
$$

without directly providing the model with the weight `2` or bias `1`.

## Model

The model has the form:

$$
\hat{y} = wx + b
$$

where `w` and `b` are learned during training.

## Training Process

The model is trained using the following workflow:

1. Forward pass
2. Loss calculation
3. Gradient reset
4. Backpropagation
5. Parameter update

Mean Squared Error (MSE) is used as the loss function, and Stochastic Gradient Descent (SGD) is used as the optimizer.

## Results

After training for 1500 epochs, the model learned approximately:

- Weight: `1.999`
- Bias: `1.002`
- Final loss: approximately `1.05e-6`

The expected values were:

- Weight: `2`
- Bias: `1`

The learned model therefore closely approximates the original relationship.

## Concepts Practiced

- PyTorch tensors
- Linear models
- Forward propagation
- Mean Squared Error (MSE)
- Automatic differentiation
- Backpropagation
- Gradient descent
- Optimizers
- Training loops

## Connection to PINNs

This exercise serves as a foundation for studying **Physics-Informed Neural Networks (PINNs)**.

In a standard neural network, the loss function measures the difference between predictions and observed data. In a PINN, differential equations and physical constraints can also be incorporated into the loss function.

Understanding PyTorch's training loop and automatic differentiation is therefore an important first step toward implementing PINNs for differential equations.

## Notebook

The complete implementation and training results are available in:

[View the PyTorch Linear Regression Notebook](./pytorch_linear_regression.ipynb)
