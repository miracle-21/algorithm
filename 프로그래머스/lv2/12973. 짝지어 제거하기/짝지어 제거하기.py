from collections import deque

def solution(s):
    q = deque(s)
    lst = []
    while q:
        if len(lst) == 0:
            lst.append(q.popleft())
            continue
        elif lst[-1] == q[0]:
            del lst[-1]
            q.popleft()
        else:
            lst.append(q.popleft())
    if lst:
        return 0
    else:
        return 1
            