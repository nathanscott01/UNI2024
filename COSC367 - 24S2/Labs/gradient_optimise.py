"""
Nathan Scott
COSC367 Lab 7
Gradient Optimise
"""


def gradient_optimize(x0, gradient, step_factor, direction, iterations):
    """Return an optimal point x* in R^n"""
    for i in range(iterations):
        x0 = x0 + direction * step_factor * gradient(x0)
    return x0
