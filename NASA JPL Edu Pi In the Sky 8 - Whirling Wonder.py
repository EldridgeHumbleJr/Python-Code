import math

#Author: Eldridge Humble Jr.

#Date: March 31, 2021

#Purpose: The purpose of this program is to answer the question from JPL Edu's activity Pi In the Sky 8: Whirling
#Wonder "How fast - in rotations per minute -  do Ingenuity's blades spin?". It also answers the question "How
#does that compare to the typical helicopter on Earth?"

#Activity Address: https://www.jpl.nasa.gov/edu/teach/activity/pi-in-the-sky-8/

#This line of code sets the constant value of 250. This number is how many radians per second is required
#for Ingenuity's blades to spin in order to lift it off of the ground in Mars' atmosphere
radiansPerSecond = float(250)

#This line of code converts radians/sec to radians/min since the final answer will be in revolutions per minute.
radiansPerMinuteConversion = float(radiansPerSecond * 60)

#This line of code converts radians to revolutions by dividing the radians per minute value by 2 times Pi.
radiansToRevolutionsConversion = float(radiansPerMinuteConversion/(2 * math.pi))
print("Ingenuity's blades spinning at 250 radians per second is equivalent to " + str(radiansToRevolutionsConversion) + " revolutions per minute")

#This line of code sets the constant value of how many Revolutions Per Minute are required to lift the typical Earth helicopter off of the ground.
typicalEarthHelicopterRPM = float(500)

#This line of code calculates the comparison between the RPM of the Ingenuity helicopter on Mars and a typical helicopter on Earth.
ingenuityAndEarthHelicopterComparison = radiansToRevolutionsConversion / typicalEarthHelicopterRPM


print("The blades of the Ingenuity helicopter spin " + str(ingenuityAndEarthHelicopterComparison) + " faster than the typical helicopter on Earth.")
