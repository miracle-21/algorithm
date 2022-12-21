from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    avr = (sum1+sum2)/2
    result = 0
    while sum1 != sum2 != avr:
        if len(q1) == 0 or len(q2) == 0 or result > 3000000:
            return -1
        elif sum1 > sum2:
            a = q1.popleft()
            q2.append(a)
            sum1 -= a
            sum2 += a
            result += 1
        elif sum1 < sum2:
            a = q2.popleft()
            q1.append(a)
            sum2 -= a
            sum1 += a
            result += 1
    return result
        