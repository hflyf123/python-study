#概括字符集

import re


#\d  \D
#\w 单词字符 \W 非单词字符
# \s 空白字符  \S非空白字符
a = 'python 1111kava&678php'

r = re.findall('\W',a)
print(r)