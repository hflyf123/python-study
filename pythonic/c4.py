students = {
    '喜小乐': 18,
    '石敢当': 20,
    '横小五': 15
}
#将dict中的key单独拿出做list
# b = [key for key, value in students.items()]
# 将dict的key和value倒过来
# b = {value:key for key, value in students.items()}

#元组是不可变的，处理方法比较特殊
b = (key for key, value in students.items())
for x in b:
    print(x)
