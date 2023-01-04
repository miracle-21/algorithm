from itertools import combinations
import math

def solution(nums):
    lst = list(map(sum,combinations(nums,3)))
    result = 0
    for i in lst:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            result += 1
    return result