#字符集
import re

s = 'abc,acc,abc,aec,afc ahc'

# r = re.findall('a[cfd]c',s)
r = re.findall('a[^cfd]c',s)
# r = re.findall('a[c-f]c',s)
print(r)