import sys


def add(x, y):
    result = x + y
    return result


def print_code(code):  # 和内置函数重名了
    print(code)
    return code


sys.setrecursionlimit(3000)
a = add(1, 2)
b = print_code("python")
print(a, b)
