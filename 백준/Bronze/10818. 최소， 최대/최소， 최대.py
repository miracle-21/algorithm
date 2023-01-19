a = int(input())
b = input().split()
lst= []
if len(b) == a:
    for i in b:
        lst.append(int(i))
    print(min(lst), max(lst))
else:
    b = input().split()