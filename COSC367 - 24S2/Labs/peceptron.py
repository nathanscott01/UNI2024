"""
Nathan Scott
"""

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input_vector):
        activation = sum(w * x for w, x in zip(weights, input_vector)) + bias
        return 1 if activation >= 0 else 0

    return perceptron


weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))