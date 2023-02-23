'''WAP that shows a different message depending on what time of day it is morning, 
afternoon, evening, or night(24hrs). '''
t=float(input("enter the time\n"))
if t>5 and t<=12:
    print("Good Morning")
elif t>12 and t<=16:
    print("Good Noon")
elif t>16 and t<=20:
    print("Good Evening")
elif t>20 and t<5:
    print("Good Nght")
else:
    print("Goodbye")