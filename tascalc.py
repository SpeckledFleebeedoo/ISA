from ISA2 import calcISA
import math

gamma = 1.4
R = 278

def SpeedOfSound(alt):
    T = calcISA(alt)[0]
    a = math.sqrt(gamma * R * T)
    return a

def TrueAirSpeed(M, alt):
    a = SpeedOfSound(alt)
    TAS = M*a
    return TAS

if __name__ == "__main__":
    names = ["F70", "F100", "A220", "CRJX", "CRJ9", "ARJ21", "E190", "E195", "E175", "M100", "M90", "SJ100"]
    alts = [10668, 10668, 12496.8, 12496.8, 12497, 10668, 12497, 12497, 10668, 11887, 11887, 12496.8]
    Machs = [0.73, 0.73, 0.78, 0.78, 0.78, 0.78, 0.82, 0.82, 0.82, 0.78, 0.78, 0.78]

    print("Name, TAS:")
    for name, M, alt in zip(names, Machs, alts):
        TAS = TrueAirSpeed(M, alt)
        print(name, int(round(TAS, 0)))
