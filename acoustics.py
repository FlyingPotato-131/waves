import numpy as np
import matplotlib.pyplot as plt

c = 3 #speed of sound
rho = 15 #density

def lerp(prev, now, t):
	return np.array(now) - t * (np.array(now) - np.array(prev))

def sqrp(prev, now, nextt, t):
	return np.array(now) - 0.5 * t * (np.array(nextt) - np.array(prev)) + 0.5 * t**2 * (np.array(nextt) - 2 * np.array(now) + np.array(prev))

def omega(v, p):
	return -abs(c) * rho / 2 * v + p / 2, abs(c) * rho / 2 * v + p / 2

def omegaInv(w1, w2):
	return (w2 - w1) / abs(c) / rho, w2 + w1

L = 1
M = 400
# T = 0.3
T = L / abs(c)
dx = L / (M-1)
dt = 0.5 * dx / abs(c)

begin = np.zeros(M, dtype = [('v', np.float64), ('p', np.float64)])
for x in range(M // 8, M // 5):
	begin[x]['v'] = 0.1
	begin[x]['p'] = 1

now = begin.copy()
nxt = begin.copy()

for time in range(int(T / dt)):
# for time in range(15):
	if(c > 0):
		for x in range(0, M):
			wNow = omega(now[x]['v'], now[x]['p'])
			wPrev = omega(now[(x-1)%M]['v'], now[(x-1)%M]['p'])
			wNext = omega(now[(x+1)%M]['v'], now[(x+1)%M]['p'])
			# nxt[x]['v'], nxt[x]['p'] = omegaInv(*lerp(wPrev, wNow, c * dt / dx))
			nxt[x]['v'], nxt[x]['p'] = omegaInv(*sqrp(wPrev, wNow, wNext, c * dt / dx))
		nxt[0]['v'] = now[-1]['v']
		nxt[0]['p'] = now[-1]['p']
	else:
		for x in range(0, M):
			wNow = omega(now[x]['v'], now[x]['p'])
			wPrev = omega(now[(x-1)%M]['v'], now[(x-1)%M]['p'])
			wNext = omega(now[(x+1)%M]['v'], now[(x+1)%M]['p'])
			# nxt[x]['v'], nxt[x]['p'] = omegaInv(*lerp(wNow, wNext, 1 + c * dt / dx))
			nxt[x]['v'], nxt[x]['p'] = omegaInv(*sqrp(wNext, wNow, wPrev, 1 + c * dt / dx))
		nxt[-1]['v'] = now[0]['v']
		nxt[-1]['p'] = now[0]['p']
	now = nxt.copy()

fig, ax = plt.subplots()
xaxis = np.linspace(0, L, num = M)
ax.plot(xaxis, begin[0:]['v'], '--', label = "start v")
ax.plot(xaxis, begin[0:]['p'], '--', label = "start p")
ax.plot(xaxis, now[0:]['v'], '-', label = "end v")
ax.plot(xaxis, now[0:]['p'], '-', label = "end p")
plt.legend()
plt.show()
