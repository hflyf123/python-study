list_x = [1, 0, 1, 0, 0, 1]
# r = filter(lambda x: True if x==1 else False,list_x)
r = filter(lambda x: x, list_x)
print(list(r))

list_u = ['a', 'B', 'c', 'F', 'M']
r = filter(lambda x: ord(x) < 97, list_u)
print(list(r))
