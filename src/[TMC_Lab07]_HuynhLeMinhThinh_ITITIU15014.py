# Huỳnh Lê Minh Thịnh
# ITITIU15014
import math
import numpy as np
from sympy import Symbol


def problem1():
    log8 = 0.9030900
    log9 = 0.9542425
    log11 = 1.0413927
    log12 = 1.0791812

    def logA():
        return log8 + ((log12 - log8) / (12 - 8)) * (x - 8)

    def logB():
        return log9 + ((log11 - log9) / (11 - 9)) * (x - 9)

    def error(approximate, true):
        return abs((true - approximate) / true)

    x = Symbol('x')
    print("*PROBLEM 1: Linear Interpolation.")
    print("a)Compute Log10 between Log8 and Log12: ")
    print("\tLog(10) = " + str(logA().subs({x: 10})))
    print("\tRelative error: " + str(error(logA().subs({x: 10}), math.log10(10))))
    print("\nb)Compute Log10 between Log9 and Log11: ")
    print("\tLog(10) = " + str(logB().subs({x: 10})))
    print("\tRelative error: " + str(error(logB().subs({x: 10}), math.log10(10))))


def problem2():
    def newtons_interpolation(A):
        final_coefficient = list()
        ith_coefficient = list()
        temp = list(i[1] for i in A)
        final_coefficient.append(A[0, 1])  # Get b0;

        step = 1
        while final_coefficient.__len__() != np.size(A, 0):
            for i in range(temp.__len__() - 1):
                ith_coefficient.append((temp.__getitem__(i + 1) - temp.__getitem__(i)) / (A[i + step, 0] - A[i, 0]))
            final_coefficient.append(ith_coefficient.__getitem__(0))  # Get b(n-th) coefficient, {b1, b2, b3,...};
            temp = list(ith_coefficient)  # Create a temporary copy of ith coefficient
            ith_coefficient.clear()  # Clear the ith coefficient for the next loop
            step += 1
        return final_coefficient

    def polynomial():
        sub_polynomial = 1
        result = 0
        for i in range(np.size(A, 0)):
            result += sub_polynomial * list_of_coefficient.__getitem__(i)
            sub_polynomial *= (x - A[i, 0])  # Example: (x-x0)*(x-x1)*(x-x2)*(...)
        return result

    x = Symbol('x')
    # An array of [x, f(x)]; np.size(A, 0) = 7 (rows); np.size(A, 1) = 2 (columns);
    A = np.array([[0, 2],
                  [1.0, 5.4375],
                  [2.5, 7.3516],
                  [3.0, 7.5625],
                  [4.5, 8.4453],
                  [5.0, 9.1875],
                  [6.0, 12.0]])
    list_of_coefficient = newtons_interpolation(A)

    print("\n*PROBLEM 2: Newton's Interpolation Method.")
    print("\tThe polynomial: f(x) = " + str(polynomial()))
    print("\tThe result where x = 3.5, f(3.5) = " + str(polynomial().subs({x: 3.5})))


def problem3():
    def newtons_interpolation(A):
        final_coefficient = list()
        ith_coefficient = list()
        temp = list(i[1] for i in A)
        final_coefficient.append(A[0, 1])  # Get b0;

        step = 1
        while final_coefficient.__len__() != np.size(A, 0):
            for i in range(temp.__len__() - 1):
                ith_coefficient.append((temp.__getitem__(i + 1) - temp.__getitem__(i)) / (A[i + step, 0] - A[i, 0]))
            final_coefficient.append(ith_coefficient.__getitem__(0))  # Get b(n-th) coefficient, {b1, b2, b3,...};
            temp = list(ith_coefficient)  # Create a temporary copy of ith coefficient
            ith_coefficient.clear()  # Clear the ith coefficient for the next loop
            step += 1
        return final_coefficient

    def polynomial():
        sub_polynomial = 1
        result = 0
        for i in range(np.size(A, 0)):
            result += sub_polynomial * list_of_coefficient.__getitem__(i)
            sub_polynomial *= (x - A[i, 0])  # Example: (x-x0)*(x-x1)*(x-x2)*(...)
        return result

    x = Symbol('x')
    # An array of [x, f(x)]; np.size(A, 0) = 4 (rows); np.size(A, 1) = 3 (columns);
    A = np.array([[0, 0.5],
                  [1.0, 3.134],
                  [2.0, 5.3],
                  [5.5, 9.9],
                  [11.0, 10.2],
                  [13.0, 9.35],
                  [16.0, 7.2],
                  [18.0, 6.2]])
    list_of_coefficient = newtons_interpolation(A)

    print("\n*PROBLEM 3: Newton's Interpolation Method.")
    print("\tThe polynomial: f(x) = " + str(polynomial()))
    print("\tThe result where x = 8, f(8) = " + str(polynomial().subs({x: 8})))


def problem4():
    def lagrange_interpolation(A):
        result = 0
        for i in range(np.size(A, 0)):  # i from 0 to 2; [0, n) = [0, 3)
            coefficient = 1
            for j in range(1, np.size(A, 0)):  # j from 1 to 2; [1, n) = [0, 3)
                coefficient *= (x - A[(i + j) % np.size(A, 0), 0]) / (A[i, 0] - A[(i + j) % np.size(A, 0), 0])
                # coefficient *= (X - Xi+1) / (Xi - Xi+1)
            result += coefficient * A[i, 1]  # result = result + coefficient * f(xi)
        return result

    x = Symbol('x')
    # An array of [x, f(x)]; np.size(A, 0) = 3 (rows); np.size(A, 1) = 2 (columns);
    A = np.array([[1.0, 0], [4.0, 1.386294], [6.0, 1.791759]])
    # An array of [x, f(x)]; np.size(A, 0) = 7 (rows); np.size(A, 1) = 2 (columns);
    B = np.array([[0, 2],
                  [1.0, 5.4375],
                  [2.5, 7.3516],
                  [3.0, 7.5625],
                  [4.5, 8.4453],
                  [5.0, 9.1875],
                  [6.0, 12.0]])
    # An array of [x, f(x)]; np.size(A, 0) = 8 (rows); np.size(A, 1) = 2 (columns);
    C = np.array([[0, 0.5],
                  [1.0, 3.134],
                  [2.0, 5.3],
                  [5.5, 9.9],
                  [11.0, 10.2],
                  [13.0, 9.35],
                  [16.0, 7.2],
                  [18.0, 6.2]])

    print("\n*PROBLEM 4: Double check the result with Lagrange Interpolation !")
    print("a) Lagrange's Interpolation Method: ")
    print("\tThe polynomial: f(x) = " + str(lagrange_interpolation(B)))
    print("\tThe result where x = 3.5, f(3.5) = " + str(lagrange_interpolation(B).subs({x: 3.5})))
    print("\nb) Lagrange's Interpolation Method: ")
    print("\tThe polynomial: f(x) = " + str(lagrange_interpolation(C)))
    print("\tThe result where x = 8, f(8) = " + str(lagrange_interpolation(C).subs({x: 8})))


problem1()
problem2()
problem3()
problem4()
