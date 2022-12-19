import matplotlib.pyplot as plt
from ISA2 import calcISA

alt = []
T = []
p = []
rho = []
a = []

for h in range(1, 100000, 50):

    results = calcISA(h)
    alt.append(h)
    T.append(results[0])
    p.append(results[1])
    rho.append(results[2])
    a.append((1.4*287*results[0])**0.5)

plt.subplot(2, 2, 1)
plt.plot(T, alt)
plt.ylabel("Altitude")
plt.xlabel("Temperature")

plt.subplot(2, 2, 2)
plt.plot(p, alt)
plt.xlabel("Air pressure")

plt.subplot(2, 2, 3)
plt.plot(rho, alt)
plt.ylabel("Altitude")
plt.xlabel("Air density")

plt.subplot(2, 2, 4)
plt.plot(a, alt)
plt.xlabel("Speed of sound")

plt.tight_layout()
plt.show()