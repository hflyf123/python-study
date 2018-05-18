#概括字符集
#数量词
# *匹配*前面的字符0次或者无限多次
# +匹配一次或者无限多次
# ?匹配0次或者1次
import re


#\d  \D
#\w 单词字符 \W 非单词字符
# \s 空白字符  \S非空白字符
a = 'pytho0python1pythonn2'
#贪婪与非贪婪 加个?就是非贪婪模式
r = re.findall('python{1,2}?',a)
print(r)