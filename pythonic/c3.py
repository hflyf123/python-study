# 列表推导式
# 集合推导式
# map filter
# list set dict 都可以用推导式
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i**2 for i in a if i >= 5]  # 此为列表推导式,对于有选择性筛选，推荐使用列表推导式
print(b)
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {i**2 for i in a if i >= 5}
