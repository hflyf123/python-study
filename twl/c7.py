# 装饰器
import time

def f1():
    # print(time.time())
    #打印的是unix时间戳，单位是second
    print('this is a function1')


def f2():
    # print(time.time())
    #打印的是unix时间戳，单位是second
    print('this is a function2')

#对修改封闭，对拓展开放

def print_curretn_time(func):
    print(time.time())
    func()

print_curretn_time(f1)
print_curretn_time(f2)
