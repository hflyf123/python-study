#边界匹配
import re
qq = '100000001'
#4~8
r = re.findall('^10001$',qq)
print(r)