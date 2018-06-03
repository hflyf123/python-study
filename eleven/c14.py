
def f1():
    a = 10
    def f2():
        # 此时a将被python认为是一个局部变量
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()