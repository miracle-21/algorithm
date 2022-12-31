from collections import deque

def solution(s):
    s = deque(map(str,s))
    first = s.popleft()
    count1 = 1
    count2 = 0
    result = 0
    while s:
        try:
            if first == s.popleft():
                count1 += 1
            else:
                count2 += 1
            if count1 == count2:
                result += 1
                first = s.popleft()
                count1 = 1
                count2 = 0
        except:
            return result
    return result+1
    