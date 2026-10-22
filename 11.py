import matplotlib.pyplot as plt
xc, yc = map(float, input().split())
r = float(input())
x, y = map(float, input().split())
ds = (x - xc) ** 2 + (y - yc) ** 2
rs = r ** 2
eps = 1e-9
if abs(ds - rs) < eps:
    print("Точка лежит на окружности")
elif ds < rs:
    print("Точка находится внутри окружности")
else:
    print("Точка располагается за пределами окружности")
canv, ax = plt.subplots()
circle = plt.Circle((xc, yc), radius=r, color='r', fill=False)
ax.add_patch(circle)
ax.plot(x, y, 'ro', markersize=8, zorder=5)
ax.set_aspect("equal")
plt.show()