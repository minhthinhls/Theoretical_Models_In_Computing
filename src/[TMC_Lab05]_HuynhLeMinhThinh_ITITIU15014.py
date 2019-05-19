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

    golden_section_search(-2, 4, 0.008)


def problem2():
    def f(x):
        return 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4

    def parabolic_interpolation_looping(x0, x1, x2, loop_number):
        def find_x3():
            numerator = f(x0) * (x1 ** 2 - x2 ** 2) + f(x1) * (x2 ** 2 - x0 ** 2) + f(x2) * (x0 ** 2 - x1 ** 2)
            denominator = 2 * (f(x0) * (x1 - x2) + f(x1) * (x2 - x0) + f(x2) * (x0 - x1))
            return numerator / denominator

        for i in range(loop_number):
            x3 = find_x3()
            if x1 < x3:
                x0 = x1
                x1 = x3
            else:
                x2 = x1
                x1 = x3
            print("\tThe result of x3 after " + str(i + 1) + " iterations: x3 = " + str(x3))
            print("\tThe result of f(x3) after " + str(i + 1) + " iterations: f(x3) = " + str(f(x3)) + "\n")

    print("\nPROBLEM 2: ")
    print("a) Parabolic Interpolation Method: ")
    parabolic_interpolation_looping(1.75, 2, 2.5, 4)  # Loop 4 times with x0 = 1.75, x1 = 2, x2 = 2.5


def problem3():
    from sympy import Symbol, Derivative
    x = Symbol('x')

    def error_estimate(new, old, error):
        return abs((new - old) / new) > error

    def argument():
        return 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4

    def calculate_xi_plus_1(xi):
        diff_1 = Derivative(argument(), x).doit().subs({x: xi})
        diff_2 = Derivative(argument(), x, 2).doit().subs({x: xi})
        return xi - diff_1 / diff_2

    def main(initial_value, accepted_error):
        i = 1
        old_value = initial_value
        result = calculate_xi_plus_1(old_value)
        print("\tThe value of x after 1 iteration is: x = " + str(result))
        print("\tThe value of f(x) after 1 iteration is: x = " + str(argument().subs({x: result})))
        print("\tThe Estimate Error 'e' after 1 iteration is: e = " + str(abs((result - old_value) / result)) + "\n")
        while error_estimate(result, old_value, accepted_error):
            old_value = result
            result = calculate_xi_plus_1(result)
            error = abs((result - old_value) / result)
            i += 1
            print("\tThe value of x after " + str(i) + " iterations is: x = " + str(result))
            print("\tThe value of f(x) after " + str(i) + " iterations is: x = " + str(argument().subs({x: result})))
            print("\tThe Estimate Error 'e' after " + str(i) + " iterations is: e = " + str(error) + "\n")

    print("\nPROBLEM 3: ")
    print("a) Newton’s Method: ")
    main(3, 0.01)  # Initial value = 3, Estimated error < 0.01


def problem4():
    from sympy import Symbol, Derivative
    import sympy
    import numpy
    x = Symbol('x')
    y = Symbol('y')
    h = Symbol('h')

    def error_estimate(new, old, error):
        return abs((new - old) / new) < error

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

    def steepest_descent(a, b, error):
        n = 1
        while True:
            a_old = a
            b_old = b
            i = Derivative(argument(), x).doit().subs({x: a, y: b})
            j = Derivative(argument(), y).doit().subs({x: a, y: b})
            sub = argument().subs({x: a + i * h, y: b + j * h})  # A function mapping f(x,y) to g(h) by Gradient = (i,j)
            dev = Derivative(sub, h).doit()  # Take derivative of g(h) => g'(h)
            solved = sympy.solve(dev)  # Solving g'(h) = 0
            print("\n*After " + str(n) + " iterations:")
            print("\tg'(h) = " + str(dev))
            print("\tg'(h) = 0, where h = " + str(solved))
            a = a + i * solved[0]  # Update new value of x
            b = b + j * solved[0]  # Update new value of y
            print("\tx = " + str(a))
            print("\ty = " + str(b))
            print("\tF(x,y) optimized = " + str(argument().subs({x: a, y: b})))
            n += 1
            if error_estimate(a, a_old, error) and error_estimate(b, b_old, error):
                print()
                break

    print("\nPROBLEM 4: ")
    print("a) Steepest Descent Method: ")
    steepest_descent(-1, 1, 0.01)  # Initial value: (x, y) = (-1, 1); Estimated error < 0.01
    print("b) Random Search Method: ")
    random_search(1000)  # Random search with 1000 points


problem1()
problem2()
problem3()
problem4()
