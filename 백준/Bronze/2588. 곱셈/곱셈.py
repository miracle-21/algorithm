a = int(input())
b = str(input())
try: 
    for i in range(3)[::-1]:
        print(a*int(b[i]))
finally:
    print(a*int(b))