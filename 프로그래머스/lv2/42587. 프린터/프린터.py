from collections import deque

def solution(priorities, location):
    dq = deque([(i,l) for l, i in enumerate(priorities)])
    answer = 0

    while dq:
        item = dq.popleft()
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer
            

    # 정답률 20%
    # if location == max(priorities):
    #     return 1
    # while len(priorities) > 0:
    #     lst = priorities[0:priorities.index(max(priorities))]
    #     if location < priorities.index(max(priorities)):
    #         location = location + len(priorities) - priorities.index(max(priorities))
    #     else:
    #         location -= priorities.index(max(priorities))
    #     del priorities[0:priorities.index(max(priorities))]
    #     priorities += lst
    #     del priorities[0]
    # return location+1