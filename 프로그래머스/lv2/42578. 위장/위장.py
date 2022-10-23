def solution(clothes):
    dict = {}
    for i in clothes:
        try:
            dict[i[1]] += 1
        except:
            dict[i[1]] = 1
    num = 1
    lst= []
    for key, value in dict.items():
        num *= (value+1)
    return num-1