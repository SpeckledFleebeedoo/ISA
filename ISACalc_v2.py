import math
g0 = 9.80665
R = 287.0

def calcISA(h):
    data = {
        "rho" : 1.225, 
        "p" : 101325, 
        "T" : 288.15}
    layers = [[0, 11000,-0.0065], [11000, 20000, 0], [20000, 32000, 0.0010], [32000, 47000, 0.0028], [47000, 51000, 0], [51000, 71000, -0.0028], [71000, 86000, -0.0020], [86000, 100000, 0]]

    layerstouse = []
    for layer in layers:
        if layer[1] <= h:
            layerstouse.append(layer)
        elif layer[0] < h and layer[1] > h:
            layer[1] = h
            layerstouse.append(layer)
    
    for layer in layerstouse:
        if layer[2] == 0:
            data = isothermal(layer, data)
        else:
            data = gradient(layer, data)

    return data


def isothermal(layer, data):
    data["p"] = data["p"]*math.exp(-g0/(R*data["T"])*(layer[1]-layer[0]))
    data["rho"] = data["p"]/(R*data["T"])
    return data

def gradient(layer, data):
    T_old = data["T"]
    data["T"] = data["T"] + layer[2]*(layer[1]-layer[0])
    data["p"] = data["p"]*(data["T"]/T_old)**(-g0/(layer[2]*R))
    data["rho"] = data["p"]/(R*data["T"])
    return data

def roundto(num, sig_figs):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Cannot take the log of 0

def getaltitude():
    print("***ISA calculator***")
    print("1. Calculate ISA for altitude in meters")
    print("2. Calculate ISA for altitude in feet")
    print("3. Calculate ISA for altitude in FL")
    while True:		#Infinite loop, broken if one of the if statements is satisfied
        userchoice = input("Enter your choice: ")	#Input for mode
        if userchoice == "1":
            h = float(input("Enter altitude [m]: ")) #altitude in m, no conversion
            break
        if userchoice == "2":
            h = float(input("Enter altitude [ft]: "))
            h = h*0.3048 #immediate conversion to m
            break
        if userchoice == "3":
            h = float(input("Enter altitude [FL]: "))
            h = h*30.48 #immediate conversion to m
            break
        else:
            print("Invalid input")	#Input does not match one of the choices
    return h

def printresults(results):
    T = roundto(results["T"], 5)
    p = roundto(results["p"], 6)
    rho = roundto(results["rho"], 5)
    print(f"Temperature: {T}")
    print(f"Pressure:    {p}")
    print(f"Density:     {rho}")

def main():
    h = getaltitude()
    results = calcISA(h)
    printresults(results)


if __name__ == "__main__":
    main()