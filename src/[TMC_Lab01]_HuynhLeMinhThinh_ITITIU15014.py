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
        value = input("Enter the number: ")
        values = list(value.split(","))
        tuples = tuple(value.split(","))
        print(values)
        print(tuples)


def problem5():
    class IOString():
        def __init__(self):
            self.str1 = ""

        def get_String(self):
            self.str1 = input()

        def print_String(self):
            print(self.str1.upper())

    print("Enter the string: ")
    str1 = IOString()
    str1.get_String()
    str1.print_String()


def problem6():
    import math
    while True:
        results = list()
        value = input("Enter the number: ")
        values = list(value.split(","))
        for x in values[:]:
            results.append(round(math.sqrt((2 * 50 * int(x) / 30))))
        print(','.join([str(i) for i in results]))
        # results.clear()


def problem7():
    while True:
        value = input("Enter the number X,Y respectively: ")
        values = list(value.split(","))
        X = int(values.__getitem__(0))
        Y = int(values.__getitem__(1))
        matrix = [[X * Y for Y in range(0, Y)] for X in range(0, X)]
        print(matrix)


def problem8():
    while True:
        value = input("Enter the words: ")
        values = list(value.split(","))
        values.sort()
        print(','.join([str(i) for i in values]))


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
    def remove_duplicates(values):
        output = list()
        seen = set()
        for value in values:
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output

    while True:
        string = ""
        value = input("Enter the words: ")
        values = list(value.split(" "))
        values = remove_duplicates(values)
        values.sort()
        for value in values:
            string += value + " "
        print(string)

# problem1()
# problem2()
# 8
# problem3()
# 8
# problem4()
# 34,67,55,33,12,98
# problem5()
# This is the String
# problem6()
# 100,150,180
# problem7()
# 3,5
# problem8()
# without,hello,bag,world
# problem9()
# Hello world
# Practice makes perfect
# problem10()
# hello world and practice makes perfect and hello world again
