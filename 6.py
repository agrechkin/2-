year = int(input())
if year % 4 == 0 or ((year % 10 == 8) and (year//10)%10 == 0):
    print(366)
elif year % 4 != 0:
    print(365)