import numpy as np

# Set the seed for reproducibility (optional)
np.random.seed(42)

# Generate random numbers using numpy
random_numbers = np.random.randint(1, 11, size=(3, 3))  # Generates a 3x3 matrix with random integers from 1 to 10

# Generate another set of random numbers
another_random_numbers = np.random.randint(1, 11, size=(3, 3))

# Perform element-wise multiplication
result = np.multiply(random_numbers, another_random_numbers)

print("Random Numbers:")
print(random_numbers)
print("Another Set of Random Numbers:")
print(another_random_numbers)
print("Result of Multiplication:")
print(result)
