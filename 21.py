s, e = input().split('-')

letters = 'abcdefgh'

x1 = letters.index(s[0])
y1 = int(s[1])

x2 = letters.index(e[0])
y2 = int(e[1])

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print('верно')
else:
    print('неверно')