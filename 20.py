a = input()
if a[0] == 'a' or a[0] == 'c' or a[0] == 'e' or a[0] == 'g':
    if int(a[1]) % 2 == 0:
        print('белый')
    else:
        print('чёрный')
else:
    if int(a[1]) % 2 == 0:
        print('чёрный')
    else:
        print('белый')