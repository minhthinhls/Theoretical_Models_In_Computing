# Huỳnh Lê Minh Thịnh
# ITITIU15014


def problem1():
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

    print("\nPROBLEM 1: ")
    print("a) Newton’s Method: ")
    main(3, 0.01)  # Initial value = 3, Estimated error < 0.01


def problem2():
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

    print("\nPROBLEM 2: ")
    print("a) Steepest Descent Method: ")
    steepest_descent(-1, 1, 0.01)  # Initial value: (x, y) = (-1, 1); Estimated error < 0.01
    print("b) Random Search Method: ")
    random_search(1000)  # Random search with 1000 points


problem1()
problem2()
