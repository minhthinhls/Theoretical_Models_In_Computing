# Huỳnh Lê Minh Thịnh
# ITITIU15014
import sympy as sy
import numpy as np
from sympy.functions import sin, cos
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# Define the variable and the function to approximate
x = sy.Symbol('x')
f = sin(x)


# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


# Taylor approximation at x0 of the function 'function'
def taylor(functions, x0, n):
    count = 0
    total_sum = 0
    while count <= n:
        total_sum = total_sum + (functions.diff(x, count).subs(x, x0)) / (factorial(count)) * (x - x0) ** count
        count += 1
    return total_sum


# Plot results
def plot():
    x_limit = [-5, 5]
    x1 = np.linspace(x_limit[0], x_limit[1], 800)
    y1 = []
    # Approximate up until 10 starting from 1 and using steps of 2
    for j in range(1, 10, 2):
        func = taylor(f, 0, j)
        print('Taylor expansion at n=' + str(j), func)
        for k in x1:
            y1.append(func.subs(x, k))
        plt.plot(x1, y1, label='Taylor ' + str(j) + ' Order')
        y1 = []
    # Plot the function to approximate (sine, in this case)
    plt.plot(x1, np.sin(x1), label='f(x) = Sin(x)')
    plt.xlim(x_limit)
    plt.ylim([-5, 5])
    plt.xlabel('X axis label')
    plt.ylabel('Y axis label')
    plt.legend()
    plt.grid(True)
    plt.title('Taylor series approximation')
    plt.show()


plot()
