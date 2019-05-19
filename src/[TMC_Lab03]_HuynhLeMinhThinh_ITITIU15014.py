# Huỳnh Lê Minh Thịnh
# ITITIU15014


def problem1():
    def f(x):
        return -26 + 85 * x - 91 * x ** 2 + 44 * x ** 3 - 8 * x ** 4 + x ** 5

    def same_sign(a, b):
        return a * b > 0

    def error_estimate(new, old, error):
        return abs((new - old) / new) > error

    def bisect(func, low, high):
        # Find root of continuous function where f(low) and f(high) have opposite signs

        assert not same_sign(func(low), func(high))  # Throw error if 2 functions return initial same sign value.

        while error_estimate((low + high) / 2.0, low, 0.10) and error_estimate((low + high) / 2.0, high, 0.10):
            midpoint = (low + high) / 2.0
            if same_sign(func(low), func(midpoint)):
                low = midpoint
            else:
                high = midpoint

        return (low + high) / 2.0

    def false_position(func, low, high):
        # Find root of continuous function where f(low) and f(high) have opposite signs

        def formula():
            return (low * f(high) - high * f(low)) / (f(high) - f(low))

        assert not same_sign(func(low), func(high))  # Throw error if 2 functions return initial same sign value.

        while error_estimate(formula(), low, 0.002) and error_estimate(formula(), high, 0.002):
            midpoint = formula()
            if f(midpoint) < 0:
                low = midpoint
            elif f(midpoint) > 0:
                high = midpoint
            elif f(midpoint) == 0:
                return midpoint

        return formula()

    print("\nPROBLEM 1: ")
    print("a) Bisection Method: ")
    print("\tThe root which e < 10% is: x = " + str(bisect(f, 0.5, 1)))  # f(0)<0 and f(1)>0
    print("\tThe Estimate Error 'e' is: " + str(abs(bisect(f, 0.5, 1) - 0.5625) / bisect(f, 0.5, 1)))
    print("\tThe True Relative Error is: " + str(abs(bisect(f, 0.5, 1) - 0.5570255162870) / bisect(f, 0.5, 1)))
    print("b) False-position Method: ")
    print("\tThe root which e < 0.2% is: x = " + str(false_position(f, 0.5, 1.0)))  # f(0.5)<0 and f(1)>0
    print("\tEstimate Error 'e' is: " + str(abs(false_position(f, 0.5, 1) - 0.55733819) / false_position(f, 0.5, 1)))
    print("\tTrue Relative Error: " + str(abs(false_position(f, 0.5, 1) - 0.5570255162870) / false_position(f, 0.5, 1)))


def problem2():
    from sympy import Symbol, Derivative
    x = Symbol('x')

    def argument():
        return 0.95 * x ** 3 - 5.9 * x ** 2 + 10.9 * x - 6

    def derivative():
        return Derivative(argument(), x)

    def secant(xi, xi_minus_1):
        return xi - argument().subs({x: xi}) * (xi - xi_minus_1) / (
                argument().subs({x: xi}) - argument().subs({x: xi_minus_1}))

    a_result = 3.5 - argument().subs({x: 3.5}) / derivative().doit().subs({x: 3.5})
    for i in range(0, 2):
        a_result = a_result - argument().subs({x: a_result}) / derivative().doit().subs({x: a_result})

    b_result = secant(3.5, 2.5)
    b_result = secant(b_result, 3.5)
    b_result = secant(b_result, secant(3.5, 2.5))

    print("\nPROBLEM 2: ")
    print("a) Newton-Raphson Method: ")
    print("\tThe result after 3 iterations: " + str(a_result))
    print("b) Secant Method: ")
    print("\tThe result after 3 iterations: " + str(b_result))


def problem3():
    from sympy import Symbol, Derivative
    import math
    print("\nPROBLEM 3: ")

    def x_argument(x, y):
        return math.sqrt(x - y + 0.75)  # x^2 = x - y + 0.75

    def y_argument(x):
        return x ** 2 / (1 + 5 * x)  # y(1 + 5x) = x^2

    x_result = x_argument(1.2, 1.2)
    y_result = y_argument(1.2)
    for i in range(30):
        x_result = x_argument(x_result, y_result)
        y_result = y_argument(x_result)

    print("a) Fixed-point Iteration Method: ")
    print("\tThe result after 30 iterations: \n\tx = " + str(x_result) + "\n\ty = " + str(y_result))

    def u_argument():
        x = Symbol('x')
        y = Symbol('y')
        return x ** 2 - x + y - 0.75  # u(x,y) = x^2 - x + y - 0.75 = 0

    def v_argument():
        x = Symbol('x')
        y = Symbol('y')
        return x ** 2 - 5 * x * y - y  # v(x,y) = x^2 - 5xy - y = 0

    def jacobian_determinant(xi, yi):
        x = Symbol('x')
        y = Symbol('y')
        return Derivative(u_argument(), x).doit().subs({x: xi, y: yi}) * Derivative(
            v_argument(), y).doit().subs({x: xi, y: yi}) - Derivative(
            u_argument(), y).doit().subs({x: xi, y: yi}) * Derivative(v_argument(), x).doit().subs({x: xi, y: yi})

    def calculate_xi(xi, yi):
        x = Symbol('x')
        y = Symbol('y')
        numerator = u_argument().subs({x: xi, y: yi}) * Derivative(v_argument(), y).doit().subs(
            {x: xi, y: yi}) - v_argument().subs({x: xi, y: yi}) * Derivative(u_argument(), y).doit().subs(
            {x: xi, y: yi})
        return xi - numerator / jacobian_determinant(xi, yi)

    def calculate_yi(xi, yi):
        x = Symbol('x')
        y = Symbol('y')
        numerator = v_argument().subs({x: xi, y: yi}) * Derivative(u_argument(), x).doit().subs(
            {x: xi, y: yi}) - u_argument().subs({x: xi, y: yi}) * Derivative(v_argument(), x).doit().subs(
            {x: xi, y: yi})
        return yi - numerator / jacobian_determinant(xi, yi)

    x_result = calculate_xi(1.2, 1.2)
    y_result = calculate_yi(1.2, 1.2)
    for i in range(5):
        temp_x = x_result
        temp_y = y_result
        x_result = calculate_xi(temp_x, temp_y)
        y_result = calculate_yi(temp_x, temp_y)
    print("b) Newton-Raphson Method: ")
    print("\tThe result after 5 iterations: \n\tx = " + str(x_result) + "\n\ty = " + str(y_result))


problem1()
problem2()
problem3()
