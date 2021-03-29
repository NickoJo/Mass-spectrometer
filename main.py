import matplotlib.pyplot as plt

# начальные условия в СИ
B = 0.01
aem = 1.66 * 10**-27
q = 1.6 * 10**-19

for mass in range(20, 25):
    dt = 0.0000001  # шаг
    total = 100000  # кол-во точек
    x, y = [0] * total, [0] * total  # точки
    Ux, Uy = [0] * total, [0] * total  # скорости
    Ux[0], Uy[0] = 0, 1000  # нач. скорости
    m = mass * aem
    for i in range(1, total):
        # формулы скорости по проекциям х и у
        Ux[i] = Ux[i-1] + q*B*Uy[i-1]*dt/m
        Uy[i] = Uy[i-1] - q*B*Ux[i-1]*dt/m
        # засисимость координаты х и у от скорости и времени
        x[i] = x[i-1] + Ux[i-1]*dt
        y[i] = y[i-1] + Uy[i-1]*dt
        # рассматриваем участок первой полуокружности
        if y[i] < 0:
            y = y[:i]
            x = x[:i]
            break
    plt.plot(x, y, label="{} a.e.m".format(mass))
plt.title('Vx[0] = 0; Vy[0] = 1000')
plt.legend(loc="lower center")
plt.show()
