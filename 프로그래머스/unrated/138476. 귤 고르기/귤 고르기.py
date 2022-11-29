def solution(k, tangerine):
    dict = {}
    for i in tangerine:
        try:
            dict[i] += 1
        except:
            dict[i] = 1
    lst = sorted(dict.items(), key = lambda item: item[1], reverse = True)
    result = 0
    for i in lst:
        k -= i[1]
        result += 1
        if k <= 0:
            return result
    return result
        
        