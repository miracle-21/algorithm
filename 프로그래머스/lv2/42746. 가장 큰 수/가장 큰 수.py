from collections import deque

def solution(numbers):
    lst = []
    answer = ''
    for i in numbers:
        lst.append(str(i))
    lst.sort(key = lambda x : x*3, reverse=True)
    for i in lst:
        answer += i
    return str(int(answer))
    # 정답률 53.3
    # lst = []
    # for i in numbers:
    #     lst.append(str(i))
    # lst.sort(reverse=True)
    # q = deque(lst)
    # answer = ''
    # while len(q) > 1:
    #     if q[0]+q[1] > q[1]+q[0]:
    #         answer += q.popleft()
    #     else:
    #         answer += q[1]
    #         q.remove(q[1])
    # return answer + q[-1]