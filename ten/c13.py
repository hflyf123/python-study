# 
import re
language = 'PythonC#\nJavaPHP'
#4~8
#re.S可以让.去匹配换行符
r = re.findall('c#.{1}', language,re.I | re.S)
print(r)