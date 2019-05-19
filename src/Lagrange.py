# Huỳnh Lê Minh Thịnh
# ITITIU15014
import numpy as np
from sympy import Symbol


def problem4():
    def lagrange_interpolation():
        result = 0
        for i in range(np.size(A, 0)):  # i from 0 to 2; [0, n) = [0, 3)
            coefficient = 1
            for j in range(1, np.size(A, 0)):  # j from 1 to 2; [1, n) = [0, 3)
                coefficient *= (x - A[(i + j) % np.size(A, 0), 0]) / (A[i, 0] - A[(i + j) % np.size(A, 0), 0])
                # coefficient *= (X - Xi+1) / (Xi - Xi+1)
            result += coefficient * A[i, 1]  # result = result + coefficient * f(xi)
        return result

    x = Symbol('x')
    # A = np.array([[1.0, 0], [4.0, 1.386294], [6.0, 1.791759]])
    # An array of [x, f(x)]; np.size(A, 0) = 3 (rows); np.size(A, 1) = 2 (columns);
    A = np.array([[0, 0.5],
                  [1.0, 3.134],
                  [2.0, 5.3],
                  [5.5, 9.9],
                  [11.0, 10.2],
                  [13.0, 9.35],
                  [16.0, 7.2],
                  [18.0, 6.2]])

    print("\nPROBLEM 4: ")
    print("a) Lagrange's Interpolation Method: ")
    print("\nThe polynomial: f(x) = " + str(lagrange_interpolation()))
    print("The result where x = 8, f(8) = " + str(lagrange_interpolation().subs({x: 8})))


problem4()
