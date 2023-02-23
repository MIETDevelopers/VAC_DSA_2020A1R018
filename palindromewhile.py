num=int(input())
temp=num
total=0
while num:
    rem=num%10 
    num//=10
    total=total*10+rem
if total == temp:
    print("given number is palindrome")
else:
    print("not a palindrome")