n, k, m = map(int, input().split())

if m > k:
    print(m - k - 1)
if k > m:
    print(n - k + m - 1)