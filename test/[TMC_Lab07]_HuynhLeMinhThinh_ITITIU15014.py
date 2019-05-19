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


def problem2_recursive():
    def newtons_interpolation(A):
        if np.size(A, 0) == 2:
            return (A[1, 1] - A[0, 1]) / (A[1, 0] - A[0, 0])

        left_interpolation = newtons_interpolation(np.delete(A, 0, 0))
        if np.size(A, 0) == 3:
            list_1st_order.append(left_interpolation)
        elif np.size(A, 0) == 4:
            list_2nd_order.append(left_interpolation)
        elif np.size(A, 0) == 5:
            list_3rd_order.append(left_interpolation)
        elif np.size(A, 0) == 6:
            list_4th_order.append(left_interpolation)
        elif np.size(A, 0) == 7:
            list_5th_order.append(left_interpolation)
        elif np.size(A, 0) == 8:
            list_6th_order.append(left_interpolation)

        right_interpolation = newtons_interpolation(np.delete(A, np.size(A, 0) - 1, 0))
        if np.size(A, 0) == 3:
            list_1st_order.append(right_interpolation)
        elif np.size(A, 0) == 4:
            list_2nd_order.append(right_interpolation)
        elif np.size(A, 0) == 5:
            list_3rd_order.append(right_interpolation)
        elif np.size(A, 0) == 6:
            list_4th_order.append(right_interpolation)
        elif np.size(A, 0) == 7:
            list_5th_order.append(right_interpolation)
        elif np.size(A, 0) == 8:
            list_6th_order.append(right_interpolation)

        return (left_interpolation - right_interpolation) / ((A[np.size(A, 0) - 1, 0]) - A[0, 0])

    def polynomial():
        sub_polynomial = 1
        result = 0
        for i in range(np.size(A, 0)):
            result += sub_polynomial * list_of_coefficient.__getitem__(list_of_coefficient.__len__() - 1 - i)
            sub_polynomial *= (x - A[i, 0])  # Example: (x-x0)*(x-x1)*(x-x2)*(...)
        return result

    y, x, x0, x1, x2 = Symbol('y'), Symbol('x'), Symbol('x0'), Symbol('x1'), Symbol('x2')

    A = np.array([[0, 2],
                  [1.0, 5.4375],
                  [2.5, 7.3516],
                  [3.0, 7.5625],
                  [4.5, 8.4453],
                  [5.0, 9.1875],
                  [6.0, 12.0]])  # An array of [x, f(x)]; np.size(A, 0) = 7 (rows); np.size(A, 1) = 2 (columns);

    list_1st_order = list()
    list_2nd_order = list()
    list_3rd_order = list()
    list_4th_order = list()
    list_5th_order = list()
    list_6th_order = list()
    list_7th_order = list()
    list_of_coefficient = list()

    print("\n*PROBLEM 2: Newton's Interpolation Recursive Method.")
    list_6th_order.append(newtons_interpolation(A))
    if list_7th_order.__len__() != 0:
        list_of_coefficient.append(list(list_7th_order).__getitem__(list_7th_order.__len__() - 1))
    if list_6th_order.__len__() != 0:
        list_of_coefficient.append(list(list_6th_order).__getitem__(list_6th_order.__len__() - 1))
    if list_5th_order.__len__() != 0:
        list_of_coefficient.append(list(list_5th_order).__getitem__(list_5th_order.__len__() - 1))
    if list_4th_order.__len__() != 0:
        list_of_coefficient.append(list(list_4th_order).__getitem__(list_4th_order.__len__() - 1))
    if list_3rd_order.__len__() != 0:
        list_of_coefficient.append(list(list_3rd_order).__getitem__(list_3rd_order.__len__() - 1))
    if list_2nd_order.__len__() != 0:
        list_of_coefficient.append(list(list_2nd_order).__getitem__(list_2nd_order.__len__() - 1))
    if list_1st_order.__len__() != 0:
        list_of_coefficient.append(list(list_1st_order).__getitem__(list_1st_order.__len__() - 1))
    list_of_coefficient.append(A[0, 1])
    print("\tSet of 7th Order coefficient: " + str(set(list_7th_order)))
    print("\tSet of 6th Order coefficient: " + str(set(list_6th_order)))
    print("\tSet of 5th Order coefficient: " + str(set(list_5th_order)))
    print("\tSet of 4th Order coefficient: " + str(set(list_4th_order)))
    print("\tSet of 3rd Order coefficient: " + str(set(list_3rd_order)))
    print("\tSet of 2nd Order coefficient: " + str(set(list_2nd_order)))
    print("\tSet of 1st Order coefficient: " + str(set(list_1st_order)))
    print("\n\tThe polynomial: f(x) = " + str(polynomial()))
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


def problem3_recursive():
    def newtons_interpolation(A):
        if np.size(A, 0) == 2:
            return (A[1, 1] - A[0, 1]) / (A[1, 0] - A[0, 0])

        left_interpolation = newtons_interpolation(np.delete(A, 0, 0))
        if np.size(A, 0) == 3:
            list_1st_order.append(left_interpolation)
        elif np.size(A, 0) == 4:
            list_2nd_order.append(left_interpolation)
        elif np.size(A, 0) == 5:
            list_3rd_order.append(left_interpolation)
        elif np.size(A, 0) == 6:
            list_4th_order.append(left_interpolation)
        elif np.size(A, 0) == 7:
            list_5th_order.append(left_interpolation)
        elif np.size(A, 0) == 8:
            list_6th_order.append(left_interpolation)

        right_interpolation = newtons_interpolation(np.delete(A, np.size(A, 0) - 1, 0))
        if np.size(A, 0) == 3:
            list_1st_order.append(right_interpolation)
        elif np.size(A, 0) == 4:
            list_2nd_order.append(right_interpolation)
        elif np.size(A, 0) == 5:
            list_3rd_order.append(right_interpolation)
        elif np.size(A, 0) == 6:
            list_4th_order.append(right_interpolation)
        elif np.size(A, 0) == 7:
            list_5th_order.append(right_interpolation)
        elif np.size(A, 0) == 8:
            list_6th_order.append(right_interpolation)

        return (left_interpolation - right_interpolation) / ((A[np.size(A, 0) - 1, 0]) - A[0, 0])

    def polynomial():
        sub_polynomial = 1
        result = 0
        for i in range(np.size(A, 0)):
            result += sub_polynomial * list_of_coefficient.__getitem__(list_of_coefficient.__len__() - 1 - i)
            sub_polynomial *= (x - A[i, 0])  # Example: (x-x0)*(x-x1)*(x-x2)*(...)
        return result

    y, x, x0, x1, x2 = Symbol('y'), Symbol('x'), Symbol('x0'), Symbol('x1'), Symbol('x2')
    A = np.array([[0, 0.5],
                  [1.0, 3.134],
                  [2.0, 5.3],
                  [5.5, 9.9],
                  [11.0, 10.2],
                  [13.0, 9.35],
                  [16.0, 7.2],
                  [18.0, 6.2]])  # An array of [x, f(x)]; np.size(A, 0) = 4 (rows); np.size(A, 1) = 3 (columns);
    # A = np.array([[1.0, 0], [4.0, 1.386294], [6.0, 1.791759], [5.0, 1.609438]])
    list_1st_order = list()
    list_2nd_order = list()
    list_3rd_order = list()
    list_4th_order = list()
    list_5th_order = list()
    list_6th_order = list()
    list_7th_order = list()
    list_of_coefficient = list()

    print("\n*PROBLEM 3: Newton's Interpolation Recursive Method.")
    list_7th_order.append(newtons_interpolation(A))
    if list_7th_order.__len__() != 0:
        list_of_coefficient.append(list(list_7th_order).__getitem__(list_7th_order.__len__() - 1))
    if list_6th_order.__len__() != 0:
        list_of_coefficient.append(list(list_6th_order).__getitem__(list_6th_order.__len__() - 1))
    if list_5th_order.__len__() != 0:
        list_of_coefficient.append(list(list_5th_order).__getitem__(list_5th_order.__len__() - 1))
    if list_4th_order.__len__() != 0:
        list_of_coefficient.append(list(list_4th_order).__getitem__(list_4th_order.__len__() - 1))
    if list_3rd_order.__len__() != 0:
        list_of_coefficient.append(list(list_3rd_order).__getitem__(list_3rd_order.__len__() - 1))
    if list_2nd_order.__len__() != 0:
        list_of_coefficient.append(list(list_2nd_order).__getitem__(list_2nd_order.__len__() - 1))
    if list_1st_order.__len__() != 0:
        list_of_coefficient.append(list(list_1st_order).__getitem__(list_1st_order.__len__() - 1))
    list_of_coefficient.append(A[0, 1])
    print("\tSet of 7th Order coefficient: " + str(set(list_7th_order)))
    print("\tSet of 6th Order coefficient: " + str(set(list_6th_order)))
    print("\tSet of 5th Order coefficient: " + str(set(list_5th_order)))
    print("\tSet of 4th Order coefficient: " + str(set(list_4th_order)))
    print("\tSet of 3rd Order coefficient: " + str(set(list_3rd_order)))
    print("\tSet of 2nd Order coefficient: " + str(set(list_2nd_order)))
    print("\tSet of 1st Order coefficient: " + str(set(list_1st_order)))
    print("\n\tThe polynomial: f(x) = " + str(polynomial()))
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
problem2_recursive()
problem3()
problem3_recursive()
problem4()
