#动态替换
import re
def convert(value):
    mathced = value.group()
    return '!!' + mathced + '!!'

language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#',convert,language)
# language = language.replace('C#','GO')
# print(language)
print(r)

