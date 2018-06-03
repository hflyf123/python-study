from enum import Enum
from enum import IntEnum,unique

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
@unique
class VIP1(Enum):
    YELLOW = 1
    #别名
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4

# result = VIP.GREEN == 2
# 在python中枚举类型不能进行大小比较
# result = VIP.GREEN == VIP.BLACK
# result = VIP.GREEN is VIP.GREEN
# print(result)
#可以获得枚举类型的别名
# for v in VIP1.__members__.items():
#     print(v)
a = 1
print(VIP(a))
# 23种设计模式中的单例模式