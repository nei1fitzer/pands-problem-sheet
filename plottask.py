# plottask.py
# This program generates a histogram of 1000 values from a normal distribution with a mean of 5 and a standard deviation of 2.
# It also plots the function h(x) = x^3 in the range [0, 10] on separate subplots.
# author: Neil Fitzgerald
# Sources used: Stack Overflow, Python documentation, lecture notes, and OpenAI's ChatGPT for error checking when stuck.

# Import the libraries we need
import numpy as np
import matplotlib.pyplot as plt

# Set the mean and standard deviation for our normal distribution
mean = 5
std_dev = 2

# Get 1000 samples using the normal distribution
samples = np.random.normal(loc=mean, scale=std_dev, size=1000)

# Set the style for the plot (more options can be found at: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
plt.style.use('seaborn-darkgrid')

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Create a histogram to show the samples on the first subplot
n, bins, patches = ax1.hist(samples, bins=30, density=True, alpha=0.5, color='blue', label='Sample Distribution')
ax1.set_xlabel('Sample Values', fontsize=12)
ax1.set_ylabel('Density', fontsize=12)
ax1.set_title('Normal Distribution', fontsize=16)

# Define our function h(x) which is equal to x cubed
def h(x):
    return x ** 3

# Generate x values from 0 to 10
x_values = np.linspace(0, 10, 1000)

# Plot our function h(x) on the second subplot
ax2.plot(x_values, h(x_values), linewidth=2, color='red', label='Function Plot')
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('h(x)', fontsize=12)
ax2.set_title('Function Plot', fontsize=16)

# Add legends to the subplots
ax1.legend(fontsize=10, loc='upper right', frameon=True)
ax2.legend(fontsize=10, loc='upper left', frameon=True)

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.4)

# Show our awesome plot
plt.show()
