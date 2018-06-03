def f1():
    a = 10
    def f2():
        # a = 20存在时，a会被认为是一个局部变量
        return a
    return f2


f = f1()
print(f.__closure__)
