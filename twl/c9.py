import time


def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func1_name):
    print('this is a function1'+func1_name)


@decorator
def f2(func1_name, func2_name):
    print('this is a function1'+func1_name,func2_name)


@decorator
def f3(func1_name, func2_name, func3_name,**kw):
    print('this is a function1'+func1_name,func2_name, func3_name)
    print(kw)
# f1('1')
# f2('1','2')
f3('1','2','3',a=1,b=2,c=3)
