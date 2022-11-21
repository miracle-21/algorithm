def solution(s):
    dict = {'p':0, 'P':0, 'y':0, 'Y':0}
    for i in s:
        try:
            dict[i] += 1
        except:
            continue
    return dict['p'] + dict['P'] == dict['y'] + dict['Y'] 