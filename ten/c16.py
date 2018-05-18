import re
b = '183C72D1D8E67'
#match是从字符串开始的地方匹配，返回第一个满足的结果
r1 = re.match('\d',b)
# print(r1.group())
print(r1.span())
#search是搜索字符串，返回第一个满足的结果
r2 = re.search('\d',b)
print(r2)
#匹配成功后立即结束运行返回结果
r3 = re.findall('\d',b)
print(r3)