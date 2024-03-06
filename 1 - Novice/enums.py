from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4
    
print(Season.FALL)
print(Season.SUMMER.name)
print(Season.FALL.value)
print(type(Season.WINTER))
print(repr(Season.FALL))
print(list(Season))