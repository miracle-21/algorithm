def solution(participant, completion):
    dict = {}
    for i in participant:
        try:
            dict[i] += 1
        except:
            dict[i] = 1
    for i in completion:
        dict[i] -= 1
    for key, value in dict.items():
        if value != 0:
            return key
