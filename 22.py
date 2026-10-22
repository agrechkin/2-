n, k, m = map(int, input().split())

if n <= k:
    print(m * 2)
else:
    print(((2 * n + k - 1) // k) * m)