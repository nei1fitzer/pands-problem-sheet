##plottask.py
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

# Create a single plot
fig, ax = plt.subplots(figsize=(12, 6))

# Create a histogram to show the samples
n, bins, patches = ax.hist(samples, bins=30, density=True, alpha=0.5, color='blue', label='Sample Distribution')

# Define our function h(x) which is equal to x cubed
def h(x):
    return x ** 3

# Generate x values from 0 to 10
x_values = np.linspace(0, 10, 1000)

# Normalize the h(x) function by dividing its values by the maximum value of h(x) within the range
h_values_normalized = h(x_values) / max(h(x_values))

# Calculate the maximum value of the histogram
hist_max = max(n)

# Adjust the y-axis limits to accommodate both the histogram and h(x) plot
ax.set_ylim(0, hist_max + 0.1)

# Plot the normalized h(x) values on the same plot
ax.plot(x_values, h_values_normalized * hist_max, linewidth=2, color='red', label='Function Plot')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('Density / h(x)', fontsize=12)
ax.set_title('Normal Distribution and Function Plot', fontsize=16)

# Add legends to the plot
ax.legend(fontsize=10, loc='upper left', frameon=True)

# Show our awesome plot
plt.show()
