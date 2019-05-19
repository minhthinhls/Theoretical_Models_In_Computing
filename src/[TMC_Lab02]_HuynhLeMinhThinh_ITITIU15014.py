# Huỳnh Lê Minh Thịnh
# ITITIU15014

import math
import sympy as sy
import numpy as np
from sympy.functions import sin, cos
import matplotlib.pyplot as plt


def problem1(x):
    print("\nPROBLEM 1: ")
    if x == 0:
        print("The value of e^(-" + str(x) + ") is: " + str(1))
    else:
        result_1 = 0
        result_2 = 0

        for i in range(0, 20):
            result_1 += math.pow(-1, i) * (x ** i) / math.factorial(i)
        print("The value of e^(-" + str(x) + ") by method 1 is: " + str(result_1))

        for i in range(0, 20):
            result_2 += (x ** i) / math.factorial(i)
        result_2 = 1 / result_2
        print("The value of e^(-" + str(x) + ") by method 2 is: " + str(result_2))

        print("\nTrue Error of comparing 2 methods: " + str(abs(result_1 - result_2)))
        print("True Error of comparing method 1 VS true value: " + str(abs(result_1 - 0.006737947)))
        print("True Error of comparing method 2 VS true value: " + str(abs(result_2 - 0.006737947)))


def problem2():
    print("\nPROBLEM 2: ")
    plt.style.use("ggplot")

    # Factorial function
    def factorial(n):
        if n <= 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Taylor approximation at x0 of the function named 'functions'
    def taylor(functions, x0, n):
        count = 0
        total_sum = 0
        while count <= n:
            total_sum = total_sum + (functions.diff(x, count).subs(x, x0)) / (factorial(count)) * (x - x0) ** count
            count += 1
        return total_sum

    def calculate(value):
        if value == 0:
            print("The value of cos(" + str(value) + ") is: " + str(1))
            return 1
        else:
            i = 0
            total_sum = 0
            sign = 1.0
            counter = 0
            while True:
                term = sign * value ** i / math.factorial(i)
                total_sum = total_sum + term
                i += 2
                sign = -sign
                counter += 1
                if math.fabs(total_sum - math.cos(0.3 * math.pi)) <= math.pow(10, -8):
                    print("The number of terms required is: " + str(counter))
                    break
            return total_sum

    print("The approximate result is: " + str(calculate(0.3 * np.pi)))
    print("The exact value of cos is: " + str(math.cos(0.3 * math.pi)))

    x = sy.Symbol('x')
    x_limit = [-2 * np.pi, 2 * np.pi, 0.01]
    x1 = np.linspace(x_limit[0], x_limit[1], 800)
    y1 = []
    func = taylor(cos(x), 0, 10)  # 6 terms means Taylor 10th-Order series
    print('\nTaylor expansion at n = ' + str(10) + ' is: ', func)
    for k in x1:
        y1.append(func.subs(x, k))
    plt.plot(x1, y1, label='Taylor ' + str(10) + ' Order')

    x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
    # Plot the function to approximate (cosine, in this case)
    plt.plot(x, np.cos(x))
    plt.xlabel('X axis label')
    plt.ylabel('Y axis label')
    plt.title('Approximate 10th-Order Taylor Expansion and Exact Cosine')
    plt.legend(['Approximate Cosine', 'Exact Cosine'])
    plt.show()


def problem3():
    from sympy import Symbol, Derivative
    print("\nPROBLEM 3: ")
    plt.style.use("ggplot")

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

    x = Symbol('x')

    def argument():
        return (x ** 4) * (pow(math.e, -3 * x * x))

    def derivative():
        return Derivative(argument(), x)

    approximate_value = argument().subs({x: 1}) + derivative().doit().subs({x: 1}) * (0.5 - 1)
    exact_value = argument().subs({x: 0.5})
    print("The approximate value at x = 0.5 & x0 = 1 is: " + str(approximate_value))
    print("The exact value at x = 0.5 is: " + str(exact_value))

    x_limit = [-5, 5]
    x1 = np.linspace(x_limit[0], x_limit[1], 800)
    y1 = []
    func = taylor(argument(), 1, 1)  # 1 terms means Taylor 1st-Order series
    print('\nTaylor expansion at n = ' + str(1) + ' is: ', func)
    for k in x1:
        y1.append(func.subs(x, k))
    plt.plot(x1, y1, label='Taylor ' + str(1) + ' Order')

    x = np.arange(-20, 20, 0.01)
    plt.plot(x, argument())
    plt.xlabel('X axis label')
    plt.ylabel('Y axis label')
    plt.title('Approximate 1st-Order Taylor Expansion and Exact Function')
    plt.legend(['Approximate Function, x0 = 1', 'Exact Function'])
    plt.show()


def problem4():
    print("\nPROBLEM 4: ")
    plt.style.use("ggplot")

    # Define the variable and the function to approximate
    x = sy.Symbol('x')
    f = 1 / x ** 2

    # Factorial function
    def factorial(n):
        if n <= 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Taylor approximation at x0 of the function named 'functions'
    def taylor(functions, x0, n):
        count = 0
        total_sum = 0
        while count <= n:
            total_sum = total_sum + (functions.diff(x, count).subs(x, x0)) / (factorial(count)) * (x - x0) ** count
            count += 1
        return total_sum

    # Plot results
    def plot():
        x_limit = [-20, 20]
        x1 = np.linspace(x_limit[0], x_limit[1], 800)
        y1 = []
        # Plot 4th-Order Taylor series expansions with large x0
        plt.figure(1)
        # Approximate up until 4 starting from -4 and using steps of 2
        for j in range(-4, 5, 2):
            func = taylor(f, j, 4)
            print('Taylor expansions where x0 = ' + str(j) + ' is:\t', func)
            for k in x1:
                y1.append(func.subs(x, k))
            plt.plot(x1, y1, label='x0 =  ' + str(j))
            y1 = []
        plt.plot(x1, 1 / x1 ** 2, label='f(x) = 1 / (x^2)')
        plt.xlim(x_limit)
        plt.ylim([-10, 100])
        plt.xlabel('X axis label')
        plt.ylabel('Y axis label')
        plt.legend()
        plt.grid(True)
        plt.title('4th-Order Taylor series expansions with large |x0|')

        # Plot 4th-Order Taylor series expansions with small x0
        plt.figure(2)
        # Approximate up until 0.5 starting from -0.5 and using steps of 0.5
        for j in np.arange(-0.5, 1.0, 0.5):
            func = taylor(f, j, 4)
            print('Taylor expansions where x0 = ' + str(j) + ' is:\t', func)
            for k in x1:
                y1.append(func.subs(x, k))
            plt.plot(x1, y1, label='x0 = ' + str(j))
            y1 = []
        plt.plot(x1, 1 / x1 ** 2, label='f(x) = 1 / (x^2)')
        plt.xlim(x_limit)
        plt.ylim([-10, 100])
        plt.xlabel('X axis label')
        plt.ylabel('Y axis label')
        plt.legend()
        plt.grid(True)
        plt.title('4th-Order Taylor series expansions with small |x0|')

        # Plot 4th-Order Taylor series expansions truncation error with input x0
        plt.figure(3)
        # Approximate up with input x0
        j = float(input("\nEnter the optional number x0 for calculating truncation error: "))
        func = taylor(f, j, 4)
        print('Taylor expansions where x0 = ' + str(j) + ' is:\t', func)
        for k in x1:
            y1.append(func.subs(x, k))
        plt.plot(x1, abs(y1 - 1 / x1 ** 2), label='Truncation error with x0 = ' + str(j))

        # plt.plot(x1, 1 / x1 ** 2, label='f(x) = 1 / (x^2)')
        plt.xlim(x_limit)
        plt.ylim([-10, 100])
        plt.xlabel('X axis label')
        plt.ylabel('Y axis label')
        plt.legend()
        plt.grid(True)
        plt.title('Truncation Error of 4th-Order Taylor expansions with x0 = ' + str(j))

        plt.show()

    plot()


problem1(5)
problem2()
problem3()
problem4()
