import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# начальные условия в СИ
aem = 1.66 * 10**-27
q = 1.6 * 10**-19
Ex, Ey, Ez = 0, 0, 0
Bx, By, Bz = 0.01, 0, 0  # ИНДУКЦИЯ

x, y, z = [], [], []
for mass in range(20, 25):
    dt = 0.0000001  # шаг
    total = 5000  # кол-во точек
    x, y, z = [0] * total, [0] * total, [0] * total  # точки
    Ux, Uy, Uz = [0] * total, [0] * total, [0] * total  # скорости

    Ux[0], Uy[0], Uz[0] = 500, 1000, 0  # нач. скорости

    m = mass * aem
    for i in range(1, total):
        # формулы скорости по проекциям х и у
        Ux[i] = Ux[i - 1] + dt * q * (Ex + Uy[i - 1] * Bz - Uz[i - 1] * By) / m
        Uy[i] = Uy[i - 1] + dt * q * (Ey + Uz[i - 1] * Bx - Ux[i - 1] * Bz) / m
        Uz[i] = Uz[i - 1] + dt * q * (Ez + Ux[i - 1] * By - Uy[i - 1] * Bx) / m
        # координаты
        x[i] = x[i-1] + Ux[i-1]*dt
        y[i] = y[i-1] + Uy[i-1]*dt
        z[i] = z[i-1] + Uz[i-1]*dt
        
        # РАСКОММЕНТИРОВАТЬ,
        # если будет рассматриваться участок первой полуокружности
        '''
        if y[i] < 0:
            x = x[:i]
            y = y[:i]
            z = z[:i]
            break
        '''
    plt.plot(x, y, label="{} a.e.m".format(mass))

# 2D график
plt.xlabel("x")
plt.ylabel("y")
plt.title('Bx = 0.01, By = 0.025, Bz = 0.015\nVx[0] = 500, Vy[0] = 1000')
plt.legend(loc="lower center")

# 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
