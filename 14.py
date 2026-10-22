n = int(input())
gl = (n - (n % 493)) // 493
skil = ((n - gl * 493) % 29) // 29
k = n - skil * 29 - gl * 493

if gl > 0:
    print(gl, 'галеонов')
if skil > 0:
    print(skil, 'скилей')
if k > 0:
    print(k, 'кантов')
5