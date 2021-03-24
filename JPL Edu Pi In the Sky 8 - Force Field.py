import math

#Author: Eldridge Humble Jr.
#Date: 3/24/2021
#Purpose: The purpose of this program is to solve the express the solutions to JPL Edu's "Pi In the Sky 8:Force Field"
#question "If Earth's magnetic flux density is 60 microteslas, what force would a hydrogen ion observe at Pi/4 radians
#from the equator?What about the north Pole?(Pi/2)

#This code segment convert microteslas to teslas
SixtyMicroTeslasToTesla = float(6 * pow(10,-5))
print("60 microteslas are equal to " + str(SixtyMicroTeslasToTesla) + " Teslas")

#This code segment convert microteslas to teslas
kmPerSecondToMeterPerSecond = float(4 * pow(10,5))
print("400 km/sec are equal to " + str(kmPerSecondToMeterPerSecond) + " m/sec")

#This code segment calculates the Lorentz force equation.
F = float((1.602 * math.pow(10,-19)) * (kmPerSecondToMeterPerSecond) * (SixtyMicroTeslasToTesla) * math.sin(math.pi/4))
print("The force of a hydrogen ion at \u03C0/4\u33AD from the equator observes " + str(F) + "N")

F2 = float((1.602 * math.pow(10,-19)) * (kmPerSecondToMeterPerSecond) * (SixtyMicroTeslasToTesla) * math.sin(math.pi/2))
print("The force of a hydrogen ion at \u03C0/2\u33AD from the equator observes " + str(F2) + "N")


 
