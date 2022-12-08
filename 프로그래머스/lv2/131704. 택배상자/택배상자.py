from collections import deque

def solution(order):
    order = deque(order)
    main = deque([i for i in range(1,len(order)+1)])
    sub = []
    num = 0
    while len(order) > 0:
        if len(main) > 0 and main[0] == order[0]:
            main.popleft()
            order.popleft()
            num += 1
        elif sub[-1:] == [order[0]]:
            sub.pop()
            order.popleft()
            num += 1
        else:
            try:
                sub.append(main.popleft())
            except:
                return num
    return num
            