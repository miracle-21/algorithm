from datetime import date

def solution(a, b):
    answer = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return answer[date(2016,a,b).weekday()]