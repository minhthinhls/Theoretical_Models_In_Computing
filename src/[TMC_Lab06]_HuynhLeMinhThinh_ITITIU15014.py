# Huỳnh Lê Minh Thịnh
# ITITIU15014
import math


def problem1():
    def r():
        return (math.sqrt(5) - 1) / 2

    def f(x):
        return 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4
        # return 2 * math.sin(x) - x ** 2 / 10

    def golden_section_search(lower, upper, error):
        def error_estimate(optimal):
            return (1 - r()) * abs((upper - lower) / optimal) > error

        def update_x1():
            return lower + r() * (upper - lower)

        def update_x2():
            return upper - r() * (upper - lower)

        def comparable():
            if f(x1) > f(x2):
                return x1
            else:
                return x2

        x1 = update_x1()
        x2 = update_x2()
        i = 1
        print("\nPROBLEM 1: ")
        print("a) Golden-Section Search Method: ")
        print("\tThe result of optimal x after 1 iteration: x = " + str(comparable()))
        print("\tThe result of optimal f(x) after 1 iteration: f(x) = " + str(f(comparable())) + "\n")

        while error_estimate(comparable()):
            if f(x2) > f(x1):
                upper = x1
                x1 = x2
                x2 = update_x2()
            else:
                lower = x2
                x2 = x1
                x1 = update_x1()

            i += 1
            print("\tThe result of optimal x after " + str(i) + " iterations: x = " + str(comparable()))
            print("\tThe result of optimal f(x) after " + str(i) + " iterations: f(x) = " + str(f(comparable())) + "\n")

        return {comparable(), f(comparable())}

    print(golden_section_search(2, 4, 0.01))  # Question 1 - Quiz 4
    #  golden_section_search(-2, 4, 0.01)


def problem2():
    from sympy import Symbol
    import numpy
    x = Symbol('x')
    y = Symbol('y')

    def argument():
        return (3.5 * x) + (2 * y) + (x ** 2) - (x ** 4) - (2 * x * y) - (y ** 2)
        # return (2 * x * y) + (2 * x) - (x ** 2) - (2 * y ** 2)

    def random_search(num_of_points):
        n = num_of_points
        a = numpy.random.rand(n, 2)  # Create an array of n elements (x, y)
        a = -2 + a * (2 - (-2))  # Normalizing value from (0, 1) to (-2, 2)
        maximum = argument().subs({x: a[0, 0], y: a[0, 1]})
        for i in range(0, n):
            result = argument().subs({x: a[i, 0], y: a[i, 1]})
            if result > maximum:
                maximum = result
        print("\nThe maximum of f(x) by random search on " + str(n) + " tries: " + str(maximum))

    print("\nPROBLEM 2: ")
    print("a) Random Search Method: ")
    random_search(1000)  # Random search with 1000 points


problem1()
problem2()
