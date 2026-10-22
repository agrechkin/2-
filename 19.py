a, b = map(int, input().split('x'))
c = int(input())

if c % a == 0 or c % b == 0:
    print('да')
else:
    print('нет')