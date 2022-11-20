import math

def solution(n):
    if math.sqrt(n).is_integer() == False:
        return -1
    else:
        return (math.sqrt(n) + 1)**2