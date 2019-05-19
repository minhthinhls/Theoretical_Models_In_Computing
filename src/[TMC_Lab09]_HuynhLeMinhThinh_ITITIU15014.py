# Huỳnh Lê Minh Thịnh
# ITITIU15014
import math
import numpy as np
import numpy.linalg as LA


def problem1():
    X = [2.5, 3.5, 5.0, 6.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20]
    Y = [13.0, 11.0, 8.5, 8.2, 7.0, 6.2, 5.2, 4.8, 4.6, 4.3]

    logx = list(map(lambda x: math.log10(x), X))
    logy = list(map(lambda x: math.log10(x), Y))
    logxlogy = [x * y for x, y in zip(logx, logy)]
    logx2 = list(map(lambda x: x ** 2, logx))

    print("\n*PROBLEM 1: ")
    print("*Log(x): ")
    print(list(map(lambda x: round(x, 6), logx)))
    print(round(sum(logx), 6))

    print("\n*Log(y): ")
    print(list(map(lambda x: round(x, 6), logy)))
    print(round(sum(logy), 6))

    print("\n*Log(x)*Log(y): ")
    print(list(map(lambda x: round(x, 6), logxlogy)))
    print(round(sum(logxlogy), 6))

    print("\n*[Log(x)]^2: ")
    print(list(map(lambda x: round(x, 6), logx2)))
    print(round(sum(logx2), 6))

    I = np.array([[10.0, sum(logx)],
                  [sum(logx), sum(logx2)]])
    J = np.array([sum(logy), sum(logxlogy)])

    print("\n*A0 and A1 respectively: ")
    A = LA.solve(I, J)
    print(A)

    print("\n*a = 10^A[0]: ")
    print(round(math.pow(10, A[0]), 8))

    def y(xi):
        return math.pow(10, A[0]) * xi ** A[1]

    print("\n*The final result y(9) is: ")
    print(y(9))


problem1()
