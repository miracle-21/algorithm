from collections import deque

def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while len(deq):
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer

    # answer = 0
    # people.sort(reverse=True)
    # while len(people) > 1:
    #     if limit - people[0] < people[-1]:
    #         del people[0]
    #         answer +=1
    #     elif people[0] == people[-1]:
    #         if len(people) == 2:
    #             break
    #         else:
    #             del people[-1]
    #             del people[0]
    #             answer += 1
    #     else:
    #         for i in range(1, len(people)):
    #             if limit - people[0] >= people[i]:
    #                 del people[i]
    #                 del people[0]
    #                 answer += 1
    # answer += 1
    # return answer
