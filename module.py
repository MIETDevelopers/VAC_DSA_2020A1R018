#math module are:
#Euler's Number
#pi
#Tau
#Infinity
#Not a number(NaN)
import math
#Euler's Number
print("Euler's Number is :",math.e)
print("\n")
#pi
print("pi value is :",math.pi)
#area of circle using pi
r=int(input("Enter the value of the radius:\n"))
pie=math.pi
print("Area is: ",pie*r*r)
print("\n")
#Tau
print("The value of Tau is:\n",math.tau)
#Infinity
# Print the positive infinity
print ("value of positive inf is:\n",math.inf)
# Print the negative infinity
print ("value of negative inf is :\n",-math.inf)
print("\n")
#comparing the values of infinity with the maximum floating point value
print (math.inf > 10e108)
print (-math.inf < -10e108)
#Nan
# Print the value of nan
print ("value of nan is:\n",math.nan)
