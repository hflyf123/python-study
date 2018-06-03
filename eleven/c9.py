# def a():
#     pass

# print(type(a))
# 闭包 = 函数+环境变量（函数定义时）
# 现场
def curve_pre():
    a = 25
    def cureve(x):
        return a*x*x
    return cureve

a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))
