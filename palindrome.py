def isPalindrome(s):
    	return s == s[::-1]

s = input("enter the string which you want to check:\n")
ans = isPalindrome(s)

if ans:
	print("Yes,it is palindrome")
else:
	print("No,it is not a palindrome")
