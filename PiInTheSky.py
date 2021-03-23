#Author: Eldridge Humble Jr.
#Date: 3/23/2021
#The Purpose of this program is to answer the question "How many days will it take SMAP to
#image all of Earth’s surface? This question comes from JPL's(Jet Propulsion Laboratory) Education
#Activity Titled "Pi In the Sky". This program uses the mathematical formulas in the answer to
#calculate the answers using the Python programming language.

import math 

orbitalAltitude = float(685) #km
#Circumference = 2 x Pi x radius

#This segment of code calculates the circumference of the earth
radiusOfEarth = float(6371) #km
C = 2 * math.pi * radiusOfEarth

print("The circuference of the Earth is " + str(C))

#The following segment of code calculates the number of orbits will be required to photograph the entire earth.
widthOfSwath = float(2000) #km
numberOfOrbits = C / widthOfSwath
print("The number of orbits require by SMAP to photograph the entire earth is " + str(numberOfOrbits) )

# The next segment of code calculates the orbiatal period of SMAP
#Orbital Period = Circumference / Orbital Velocity

#Since SMAP is orbiting 685km above the earth, then the circumference of its orbit is calcuated as follows
circumferenceOfSmapOrbit = 2 * math.pi * (radiusOfEarth + orbitalAltitude)
print("The circumference Of SMAP Orbit is " + str(circumferenceOfSmapOrbit))

# The next segment of code calculates the orbital velocity of SMAP
#Vc = Sqrt(GM/R)

gravityValues = float(6.67 * pow(10,-11)) 
massOfEarth = float(5.976 * pow(10,24))
radiusOfSmapOrbit = radiusOfEarth + orbitalAltitude

#I do not yet know how to convert the value of the following orbital velocity value to km/hr so I just hard coded the correct value in the line of code after it.
orbitalVelocity = math.sqrt((gravityValues * massOfEarth) / radiusOfSmapOrbit)
orbitalVelocityAfterUnitConversion = float(27057) #km/hr 
print("The orbital velocity of SMAP Orbit is " + str(orbitalVelocity))

# The next segment of code calculates the orbital period of SMAP
orbitalPeriod = circumferenceOfSmapOrbit / orbitalVelocityAfterUnitConversion
print("The orbital period of SMAP is " + str(orbitalPeriod))

numberOfHoursToPhotoEntireEarth = numberOfOrbits * orbitalPeriod
ToDaysConversion = numberOfHoursToPhotoEntireEarth / 24
print("The number of days for SMAP to photograph th entire earth " +str(ToDaysConversion))

