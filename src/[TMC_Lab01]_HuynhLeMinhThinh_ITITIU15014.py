# Huỳnh Lê Minh Thịnh
# ITITIU15014


def problem1():
    string = ""
    for x in range(2000, 3200):
        if (x % 7 == 0) and (x % 5 != 0):
            string += str(x) + ','
    print(string)


def problem2():
    while True:
        result = 1
        x = int(input("Enter the number: "))
        for x in range(1, x + 1):
            result *= x
        print(result)


def problem3():
    while True:
        x = int(input("Enter the number: "))
        d = dict()
        for x in range(1, x + 1):
            d[x] = x * x
        print(d)


def problem4():
    while True:
        values = input("Enter the number: ")
        print(list(values.split(",")))
        print(tuple(values.split(",")))


def problem5():
    print(input("Enter the string: ").upper())


def problem6():
    import math
    while True:
        numbers = input("Enter the number: ").split(",")
        results = list(map(lambda x: round(math.sqrt((2 * 50 * int(x) / 30))), numbers))
        print(','.join([str(i) for i in results]))


def problem7():
    while True:
        values = input("Enter the number X,Y respectively: ").split(",")
        X = int(values[0])
        Y = int(values[1])
        matrix = [[X * Y for Y in range(Y)] for X in range(X)]
        print(matrix)


def problem8():
    while True:
        values = input("Enter the words: ").split(",")
        print(','.join(sorted(values)))


def problem9():
    while True:
        lines = []
        print("Please write down your text: ")
        while True:
            line = input()
            if line:
                lines.append(line.upper())
            else:
                break
                # Enter 2 times to exit the loop
        for line in lines:
            print(line)


def problem10():
    while True:
        string = input("Enter the words: ")
        print(" ".join(sorted(set(string.split()))))


# problem1()
# problem2()
"""8"""
# problem3()
"""8"""
# problem4()
"""34,67,55,33,12,98"""
# problem5()
"""This is the String"""
# problem6()
"""100,150,180"""
# problem7()
"""3,5"""
# problem8()
"""without,hello,bag,world"""
# problem9()
"""
Hello world
Practice makes perfect
"""
# problem10()
"""hello world and practice makes perfect and hello world again"""
