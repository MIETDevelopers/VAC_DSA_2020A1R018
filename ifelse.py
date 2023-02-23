M=int(input("enter your marks\n"))
if M<40:
    print("Student is fail")
if M<50 and M>=40:
    print('grade is C')
elif M>=50 and M<60:
    print('grade is B')
else:
    print("grade is A")