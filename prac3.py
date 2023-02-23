'''WAP to calculate the elec. bill(accept number of unit from user) according to the following criteria-
i)first 100 unit no price
ii)next 100 unit 6rupees per unit
iii)after 200 unit 8rupees per unit
A fixed charge of rupees 40 is applicable to all
Ip: 95 OP:40rs only
Ip:165 Op:430rs only
Ip: 225 Op:840rs only'''
x=int(input("enter the number of units consumed\n"))
if x<=100:
    print("Your bill is rupees 40 only")
elif x>100 and x<=200:
    print('your bill is Rs',(x-100)*6+40,'only')
else:
    print('your bill is Rs',(x-200)*8+(100*6)+4)