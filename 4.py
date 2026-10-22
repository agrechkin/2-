team1, team2 = map(int, input().split(":"))
if team1 > team2:
    print(1)
elif team2 > team1:
    print(2)
else:
    print(0)