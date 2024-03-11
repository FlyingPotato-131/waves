import numpy as np
import matplotlib.pyplot as plt

L = 1
l = 0.01
M = 1000
T = 300
dx = L / (M-1)
dt = 0.5 * dx / l

begin = np.zeros(M)
for x in range(1, M // 5):
	begin[x] = 1
linapprox = np.copy(begin)
sqrapprox = np.copy(begin)

for time in range(int(T / dt)):
	prev = linapprox[0]
	for x in range(1, M):
		tmp = linapprox[x]
		linapprox[x] = linapprox[x] - l * dt / dx * (linapprox[x] - prev)
		prev = tmp
	linapprox[0] = linapprox[-1]

	prev = sqrapprox[0]
	nxt = sqrapprox[2]
	for x in range(1, M):
		tmpprev = sqrapprox[x]
		tmpnxt = sqrapprox[(x + 2) % M]
		sqrapprox[x] = sqrapprox[x] - l * dt / dx * (sqrapprox[x] - prev) + (l * dt / dx)**2 * (nxt + prev - 2 * sqrapprox[x])
		prev = tmpprev
		nxt = tmpnxt
	sqrapprox[0] = linapprox[-1]

fig, ax = plt.subplots()
xaxis = np.linspace(0, L, num = M)
ax.plot(xaxis, begin, '--', label = "begin")
ax.plot(xaxis, linapprox, label = "linear approximation")
ax.plot(xaxis, sqrapprox, label = "square approximation")
plt.legend()
plt.show()
