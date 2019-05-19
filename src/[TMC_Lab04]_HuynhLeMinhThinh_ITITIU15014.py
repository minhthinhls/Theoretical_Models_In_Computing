# Huỳnh Lê Minh Thịnh
# ITITIU15014
import pprint
import numpy
import scipy  # Import Science Python
import scipy.linalg as LA  # SciPy Linear Algebra Library


def problem1():
    def error_estimate(new, old, error):
        return abs((new - old) / new) < error

    def gauss_seidel_without_relaxation(A, B, x, error):
        def stop_condition():
            a = error_estimate(x[0], x_old[0], error)
            b = error_estimate(x[1], x_old[1], error)
            c = error_estimate(x[2], x_old[2], error)
            return a and b and c

        L = numpy.tril(A)  # Lower triangle of A matrix
        U = A - L  # Upper triangle of A matrix
        i = 0
        while True:
            x_old = x
            x = numpy.dot(numpy.linalg.inv(L), B - numpy.dot(U, x))
            i += 1
            print("\nThe result of x1, x2, x3 respectively after " + str(i).zfill(2) + " iterations is: ")
            print(x)
            if stop_condition():
                return x
        return x

    def gauss_seidel_with_relaxation(A, B, x, error, relaxation):
        def stop_condition():
            a = error_estimate(x[0], x_old[0], error)
            b = error_estimate(x[1], x_old[1], error)
            c = error_estimate(x[2], x_old[2], error)
            return a and b and c

        L = numpy.tril(A)  # Lower triangle of A matrix
        U = A - L  # Upper triangle of A matrix
        i = 0
        while True:
            x_old = x
            x = numpy.dot(numpy.linalg.inv(L), B - numpy.dot(U, x))
            x = numpy.dot(relaxation, x) + numpy.dot((1.0 - relaxation), x_old)
            i += 1
            print("\nThe result of x1, x2, x3 respectively after " + str(i).zfill(2) + " iterations is: ")
            print(x)
            if stop_condition():
                return x
        return x

    A = numpy.array([[6.0, -1.0, -1.0], [6.0, 9.0, 1.0], [-3.0, 1.0, 12.0]])  # To Pivot Before Calculate
    B = numpy.array([3.0, 40.0, 50.0])  # To Pivot Before Calculate
    x_init = [1, 1, 1]  # Create initial value of [x1, x2, x3] = [1, 1, 1]

    print("PROBLEM 1: ")
    print("a) Gauss-Seidel Without Relaxation Method: ")
    print("\nThe final result of x1, x2, x3:\n" + str(gauss_seidel_without_relaxation(A, B, x_init, 0.05)))
    print("\nDouble checks the result by Linear Algebra method:\n" + str(LA.solve(A, B)))
    print("\nb) Gauss-Seidel With Relaxation Method: ")
    print("\nThe final result of x1, x2, x3:\n" + str(gauss_seidel_with_relaxation(A, B, x_init, 0.05, 0.95)))
    print("\nDouble checks the result by Linear Algebra method:\n" + str(LA.solve(A, B)))


def problem2():
    def jacobi(A, B, x, n):
        D = numpy.diag(A)
        R = A - numpy.diagflat(D)
        for i in range(n):
            x = (B - numpy.dot(R, x)) / D
            print("\nThe result of x1, x2, x3 respectively after " + str(i + 1).zfill(2) + " iterations is: ")
            print(x)
        return x

    def gauss_seidel(A, B, x, n):
        L = numpy.tril(A)  # Lower triangle of A matrix
        U = A - L  # Upper triangle of A matrix
        for i in range(n):
            x = numpy.dot(numpy.linalg.inv(L), B - numpy.dot(U, x))
            print("\nThe result of x1, x2, x3 respectively after " + str(i + 1).zfill(2) + " iterations is: ")
            print(x)
        return x

    A = numpy.array([[4.0, 1.0, -1.0], [2.0, 7.0, 1.0], [1.0, -3.0, 12.0]])  # To Pivot Before Calculate
    B = numpy.array([3.0, 19.0, 31.0])  # To Pivot Before Calculate
    x_init = [1, 1, 1]  # Create initial value of [x1, x2, x3] = [1, 1, 1]

    print("PROBLEM 2: ")
    print("a) Jacobi Method: ")
    print("\nThe final result of x1, x2, x3:\n" + str(jacobi(A, B, x_init, 16)))
    print("\nDouble checks the result by Linear Algebra method:\n" + str(LA.solve(A, B)))
    print("\nb) Gauss-Seidel Method: ")
    print("\nThe final result of x1, x2, x3:\n" + str(gauss_seidel(A, B, x_init, 8)))
    print("\nDouble checks the result by Linear Algebra method:\n" + str(LA.solve(A, B)))


problem1()
problem2()
