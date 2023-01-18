hr, min = map(int, input().split())
if min >= 45:
    print(hr, min-45)
else:
    if hr > 0:
        print(hr-1, min+60-45)
    else:
        print(23, min+60-45)