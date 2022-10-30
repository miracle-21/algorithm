def solution(x):
    x = str(x)
    num = 0
    for i in range(len(x)):
        num += int(x[i])
    return (int(x)/num).is_integer()