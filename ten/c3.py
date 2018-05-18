import re

a = 'C0C++7Java8C#Python6Javascript'

r = re.findall('\D', a)
print(r)
