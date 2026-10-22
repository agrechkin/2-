n = int(input())

if 11 <= n <= 14:
    print(n, "попугаев")
else:
    lnum = n % 10
    if lnum == 1:
        print(n, "попугай")
    elif 2 <= lnum <= 4:
        print(n, "попугая")
    else:
        print(n, "попугаев")