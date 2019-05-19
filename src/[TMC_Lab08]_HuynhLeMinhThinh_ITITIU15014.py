# Huỳnh Lê Minh Thịnh
# ITITIU15014
import math
import numpy as np
from sympy import Symbol


def problem1():
    def lagrange_interpolation():
        result = 0
        for i in range(np.size(A, 0)):  # i from 0 to 5; [0, n) = [0, 6)
            coefficient = 1
            for j in range(1, np.size(A, 0)):  # j from 1 to 5; [1, n) = [0, 6)
                coefficient *= (x - A[(i + j) % np.size(A, 0), 0]) / (A[i, 0] - A[(i + j) % np.size(A, 0), 0])
                # coefficient *= (X - Xi+1) / (Xi - Xi+1)
            result += coefficient * A[i, 1]  # result = result + coefficient * f(xi)
        return result

    x = Symbol('x')
    # An array of [x, f(x)]; np.size(A, 0) = 6 (rows); np.size(A, 1) = 2 (columns);
    A = np.array([[1.0, 3.0],
                  [2.0, 6.0],
                  [3.0, 19.0],
                  [5.0, 99.0],
                  [7.0, 291.0],
                  [8.0, 444.0]])

    print("\n*PROBLEM 1: ")
    print("a) Lagrange's Interpolation Method: ")
    print("\nThe polynomial: f(x) = " + str(lagrange_interpolation()))
    print("The result where x = 4, f(4) = " + str(lagrange_interpolation().subs({x: 4})))


def problem2():
    def getValue(x0):
        polynomial = 0
        for i in range(np.size(A, 0)):
            if x0 > A[i, 0]:
                continue
            elif x0 == A[i, 0]:
                return A[i, 1]
            elif x0 < A[i, 0]:
                pos = i  # Spline number i-th
                break

        for i in range(3):
            coefficient = coefficients[pos - 1][i]
            polynomial += coefficient * (x ** (2 - i))

        print("\n*The polynomial at x = " + str(x0) + ", f(x) = " + str(polynomial))
        print("*The result where x = " + str(x0) + ", f(" + str(x0) + ") = " + str(polynomial.subs({x: x0})))

        return polynomial.subs({x: x0})

    x = Symbol('x')
    # An array of [x, f(x)]; np.size(A, 0) = 6 (rows); np.size(A, 1) = 2 (columns);
    A = np.array([[1.0, 3.0],
                  [2.0, 6.0],
                  [3.0, 19.0],
                  [5.0, 99.0],
                  [7.0, 291.0],
                  [8.0, 444.0]])

    B = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # f''(xi) = 0 -> a1 = 0.
                  # First 2 * (5) - 2 = 8 conditions for adjacent polynomials.
                  [4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 9, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 9, 3, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 25, 5, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 5, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 7, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 49, 7, 1],
                  # First & Last function through first & last point.
                  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 8, 1],
                  # (5) - 1 = 4 continuity functions of derivative.
                  [4, 1, 0, -4, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 6, 1, 0, -6, -1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 10, 1, 0, -10, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 1, 0, -14, -1, 0]])

    C = np.array([0, 6, 6, 19, 19, 99, 99, 291, 291, 3, 444, 0, 0, 0, 0])

    # Solving B{x} = C to get all coefficients {An, Bn, Cn} respectively.
    coefficients = np.linalg.solve(B, C)
    # 5 splines, each quadratic spline has 3 coefficients {An, Bn, Cn} respectively.
    coefficients = coefficients.reshape(5, 3)
    # Round off value up to 13 numbers after dot.
    coefficients = coefficients.round(13)

    print("\n*PROBLEM 2: ")
    print("a) Quadratic Splines Interpolation Method: ")
    print("*List of coefficient An, Bn, Cn respectively: " + str())
    print(coefficients)
    getValue(2.5)
    getValue(4)


problem1()
problem2()
