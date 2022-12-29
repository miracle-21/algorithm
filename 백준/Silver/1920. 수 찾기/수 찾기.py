a = input()
b = set(map(int, input().split()))
a = input()
c = list(map(int, input().split()))
for i in c:
    if i in b:
        print(1)
    else:
        print(0)