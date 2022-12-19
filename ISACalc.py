from ISA2 import calcISA
import math

def roundto(num, sig_figs):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Cannot take the log of 0

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

results = calcISA(h)
T = results[0]
p = results[1]
rho = results[2]

print("Temperature:  ", roundto(T, 5), "(", round(T-273.15, 2), "'C)")  	#prints temperature
print("Pressure:     ", roundto(p, 6), "(", round(p/101325*100), "% SL)")		#prints pressure
print("Density:      ", roundto(rho,5), "(", round(rho/1.225*100), "% SL)")	#prints density

#input("Press enter") #Press enter to finish program. Gives time to look at data after program ends.