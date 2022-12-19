import math

def calcISA(h):
    g0 = 9.80665	#Gravitational constant
    T0 = 288.15		#Sea level temperature
    R = 287.0		#Gas constant
    p0 = 101325		#Layer b5ottom pressure, altered per layer
    a = [-0.0065, 0.0010, 0.0028, -0.0028, -0.0020]     #Temperature gradients

    h1 = min(h, 11000) #Troposphere, gradient
    h0 = 0
    T1 = T0 + a[0]*(h1-h0) 			#Calculates temperature
    p1 = p0*(T1/T0)**(-g0/(a[0]*R))	#Calculates pressure
    rho1 = p1/(R*T1)				#Calculates density

    T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer

    if h>11000: #Tropopause, isothermal
        h1 = min(h, 20000)
        T1 = T0
        p1 = p0*math.exp(-g0/(R*T1)*(h1-h0))
        rho1 = p1/(R*T1)
        
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer

    if h>20000: #Stratosphere l1, gradient
        h1 = min(h, 32000)
        T1 = T0 + a[1]*(h1-h0)
        p1 = p0*(T1/T0)**(-g0/(a[1]*R))
        rho1 = p1/(R*T1)
        
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer

    if h>32000: #Stratosphere l2, gradient
        h1 = min(h, 47000)
        T1 = T0 + a[2]*(h1-h0)
        p1 = p0*(T1/T0)**(-g0/(a[2]*R))
        rho1 = p1/(R*T1)
        
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer

    if h>47000: #Stratopause, isothermal
        h1 = min(h, 51000)
        T1 = T0
        p1 = p0*math.exp(-g0/(R*T1)*(h1-h0))
        rho1 = p1/(R*T1)
        
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer

    if h>51000: #Mesosphere l1, gradient
        h1 = min(h, 71000)
        T1 = T0 + a[3]*(h1-h0)
        p1 = p0*(T1/T0)**(-g0/(a[3]*R))
        rho1 = p1/(R*T1)
        
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer

    if h>71000: #Mesosphere l2, gradient
        h1 = min(h, 86000)
        T1 = T0 + a[4]*(h1-h0)
        p1 = p0*(T1/T0)**(-g0/(a[4]*R))
        rho1 = p1/(R*T1)
    
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer
    
    if h>86000:
        h1 = min(h, 100000)
        T1 = T0
        p1 = p0*math.exp(-g0/(R*T1)*(h1-h0))
        rho1 = p1/(R*T1)
        
        T0, p0, h0 = T1, p1, h1     #Resets values for use in next layer
    
    return T0, p0, rho1