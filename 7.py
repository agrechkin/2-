d = int(input())
if (d // 1000 == d % 10) and ((d // 100)%10 == (d//10)%10):
    print("настоящее")
else:
    print("кривое")