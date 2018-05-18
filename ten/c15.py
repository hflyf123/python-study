#根据需求动态替换
import re
s = 'A8CC3721D86'
b = 'A83C72D1D8E67'
def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

def convert1(value):
    pass 

r = re.sub('\d',convert,s)
print(r)