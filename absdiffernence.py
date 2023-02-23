num=int(input())
even_digits_sum=0
odd_digits_sum=0
while num:
    rem=num%10
    if rem%2==0:
        even_digits_sum+=rem
    else:
        odd_digits_sum+=rem
    num//=10
print(abs(even_digits_sum-odd_digits_sum))