def solution(participant, completion):
    if len(participant) == len(set(participant)):
        return (list(set(participant) - set(completion)))[0]
    else:
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
        