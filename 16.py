def check(q):
    a = q % 10
    b = (q // 10) % 10
    c = (q // 100) % 10
    d = q // 1000
    if a == b or a == c or a == d or b == c or b == d or c == d:
        return 0
    else:
        return 1
pin = int(input())

if (999 < pin < 10000) and (pin < 1900 or pin > 2050) and (check(pin) == 1):
    print('Ok')
else:
    print('Error')