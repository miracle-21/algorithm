from collections import Counter

def solution(want, number, discount):
    dict = {}
    answer = 0
    for i in range(len(want)):
        dict[want[i]] = number[i]
    for i in range(len(discount)-9):
        if dict == Counter(discount[i:i+10]): 
            answer += 1
    return answer