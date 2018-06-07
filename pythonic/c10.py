class Test():
    def __len__(self):
        return True
    def __bool__(self):
        return False

test = Test()

# if test:
#     print('a')

# print(bool(None))
# print(bool([]))
# print(bool(test))
#类中如果存在bool方法，则会根据bool方法来判断，如果不存在，则会根据len方法来判断
print(len(Test()))