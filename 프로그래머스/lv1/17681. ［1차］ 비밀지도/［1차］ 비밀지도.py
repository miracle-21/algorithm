def solution(n, arr1, arr2):
    result = ''
    list = []
    for i in range(n):
        arr1[i] = format(arr1[i], f'0{n}b')
        arr2[i] = format(arr2[i], f'0{n}b')
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                result = result + "#"
            else:
                result = result + " "
        list.append(result)
        result = ''
    return list