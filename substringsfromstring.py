'''name=str(input("enter your name here"))
j=0
for i in range(len(name)):
    for j in range(i+j,len(name)+1):
        print(name[i:j])'''

strr='abcdefghijklmnopqrstuvwxyz'
vowels='aeiou'
key=6
ex=input()
for i in range(len(ex)):
    for j in range(i+1,len(ex)+1):
        total=0
        for a in (ex[i:j]):
            if a in vowels:
                value=strr.index(a)
                total+=value+1
        if total==key:
            print(ex[i:j])
            