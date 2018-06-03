# -*- coding: utf-8 -*

# 匿名函数
# lambda表达式

def add(x, y):
    return x + y

print(add(1,2))

f = lambda x, y: x + y
print(f(1,2))

# lambda parameter_list: expression

#三元表达式
# x > y ? x : y
# 条件为真时返回的结果 if 条件判断 else 条件为假时返回的结果
# x if x > y else y
x = 2
y = 1
r = x if x > y else y
print(r)