#组
import re
a = 'PythonPythonPythonPyhonPython'
#()中间的字符是且的关系，[]是或的关系
r = re.findall('(Python){3}(JS)',a)
print(r)
