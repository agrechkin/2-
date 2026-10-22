n = int(input())

if n <= 10:
    print(n - 1)
elif n <= 190:
    i = n - 11
    x = 10 + i // 2
    d = i % 2
    if d == 0:
        print(x // 10)
    else:
        print(x % 10)
else:
    i = n - 191
    x = 100 + i // 3
    d = i % 3
    if d == 0:
        print(x // 100)
    elif d == 1:
        print((x // 10) % 10)
    else:
        print(x % 10)