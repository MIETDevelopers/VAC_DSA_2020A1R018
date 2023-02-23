a = {}
n=int(input("number of elements:"))
for i in range(n):
    k = input("enter key:")
    v = input("enter the value:")
    a.update({k:v})
print(a)
b=input("enter the key you want to delete:")
del a[b]
print(a)