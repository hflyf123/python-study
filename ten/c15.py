#根据需求动态替换
import re
s = 'A8CC3721D86'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'


r = re.sub('\d',convert,s)
print(r)