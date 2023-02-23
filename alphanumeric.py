'''s='B4A1D3'
alphabets=''
digits=''
for ch in s:
    if ch.isalpha():
        alphabets+=ch
    else:
        digits+=ch
output=''
for ch in sorted(alphabets):
    output=output+ch
for ch in sorted(digits):
    output=output+ch
print(output) '''


input_str = "a3b2c5"
output_str = " "

for i in range(0,len(input_str),2):
    char = input_str[i]
    count = int(input_str[i+1])
    output_str += char * count
    
print("output:",output_str)