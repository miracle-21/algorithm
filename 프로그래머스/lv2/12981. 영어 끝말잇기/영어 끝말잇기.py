from collections import deque
from math import ceil

def solution(n, words):
    lst = []
    q = deque(words)
    lst.append(q.popleft())
    while q:
        if q[0][0] == lst[-1][-1] and q[0] not in lst:
            lst.append(q.popleft())
        else:
            lst.append(q.popleft())
            if len(lst)%n == 0:
                return [n ,ceil(len(lst) / n)]
            return [len(lst)%n ,ceil(len(lst) / n)]
    return [0,0]
