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
    
    # 1. 효율성 테스트 0%
    # for i in participant:
    #     if participant.count(i) != completion.count(i):
    #         return i
    
    # 2. 효율성 테스트 0%
    # lst = participant+completion
    # for i in lst:
    #     if lst.count(i) % 2 == 1:
    #         return i