import re
a = 'C0C++7Java8C#Python6Javascript'
r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含python')
else:
    print('No')
print(r)
