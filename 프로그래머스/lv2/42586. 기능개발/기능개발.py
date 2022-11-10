def solution(progresses, speeds):
    num = 0
    time = 0
    lst = []
    while progresses:
        while progresses[0] < 100:
            progresses[0] += speeds[0]
            num += 1
        progresses.pop(0)
        speeds.pop(0)
        if time >= num:
            lst[-1] += 1
        else:
            time = num
            lst.append(1)
        num = 0
    return lst