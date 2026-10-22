a, b = map(int, input().split('x'))
c, d, e = map(int, input().split('x'))
if a * b >= c * d or a * b >= c * e or a * b >= d * e:
    print('да')
else:
    print('нет')