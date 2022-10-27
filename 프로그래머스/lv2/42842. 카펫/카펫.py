def solution(brown, yellow):
    i = 0
    while True:
        i += 1
        if yellow % i == 0:
            if int((yellow/i)+2) * int(i+2) == brown+yellow:
                return [int(yellow/i)+2,int(i+2)]