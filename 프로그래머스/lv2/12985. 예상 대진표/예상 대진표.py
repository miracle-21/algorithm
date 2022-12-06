import math

def solution(n,a,b):
    answer = 1
    while True:
        if max(a,b)%2 == 0 and max(a,b)-min(a,b) == 1:
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1
    return answer
        