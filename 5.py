total1, total2, total3 = map(int, input().split())

if total1 >= total2 and total1 >= total3:
    print(total1)
elif total2 >= total1 and total2 >= total3:
    print(total2)
elif total3 >= total2 and total3 >= total1:
    print(total3)