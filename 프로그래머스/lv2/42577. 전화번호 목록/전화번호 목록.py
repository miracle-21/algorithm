from collections import deque

def solution(phone_book):
    phone_book.sort()
    q = deque(phone_book)
    while len(q) > 1:
        num = q.popleft()
        if num == q[0][:len(num)]:
            return False
    return True
    