# map


list_x = [1,2,3,4,5,6,7,8]

def f1(x):
    return  x * x

r = map(f1,list_x)
print(list(r))