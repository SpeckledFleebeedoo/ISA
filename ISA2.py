import math

g0 = 9.80665
R = 287.0

def iso(h0, h1, T0, p0):
    p1 = p0*math.exp(-g0/(R*T0)*(h1-h0))
    rho1 = p1/(R*T0)
    return T0, p1, rho1

def gradient(h0, h1, a, T0, p0):
    T1 = T0 + a*(h1-h0)
    p1 = p0*(T1/T0)**(-g0/(a*R))
    rho1 = p1/(R*T1)
    return T1, p1, rho1

def calcISA(h):
        a = [-0.0065, 0, 0.0010, 0.0028, 0, -0.0028, -0.0020, 0]
        T1 = 288.15
        p1 = 101325
        hights = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000, 100000]
        loops = 0

        for y in range(len(hights)):
                if h>hights[y]:
                        loops += 1

        for i in range(loops):
                if a[i] == 0:           #isothermal
                        h0 = hights[i]
                        h1 = min(h, hights[i+1])
                        T0 = T1
                        p0 = p1
                        result = iso(h0, h1, T0, p0)
                        T1 = result[0]
                        p1 = result[1]

                else:                   #gradient
                        h0 = hights[i]
                        h1 = min(h, hights[i+1])
                        T0 = T1
                        p0 = p1
                        result = gradient(h0, h1, a[i], T0, p0)
                        T1 = result[0]
                        p1 = result[1]
        return result