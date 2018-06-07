import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    print('this is a function1')

f1()

# def decorator1(func):
#     def wrapper():
#         pass
#         func
#     return wrapper