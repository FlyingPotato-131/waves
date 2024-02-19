import numpy as np
import matplotlib.pyplot as plt

L = 1
l = 0.01
M = 1000
T = 30
dx = L / (M-1)
dt = 0.5 * dx / l

begin = np.zeros(M)
for x in range(1, 200):
	begin[x] = 1
current = np.copy(begin)

for time in range(int(T / dt)):
	# for x in range(M - 1, 0, -1):
	prev = current[0]
	for x in range(1, M):
		tmp = current[x]
		current[x] = current[x] - l * dt / dx * (current[x] - prev)
		prev = tmp
	current[0] = 0

fig, ax = plt.subplots()
xaxis = np.linspace(0, L, num = M)
ax.plot(xaxis, begin, '--', label = "begin")
ax.plot(xaxis, current, label = "end")
plt.legend()
plt.show()
