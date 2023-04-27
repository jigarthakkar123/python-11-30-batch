s=input("Enter String : ")
space=0
digit=0
alpha=0
special=0

for i in s:
    if i.isspace():
        space=space+1
    elif i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
    else:
        special+=1

print("Total Alphabets : ",alpha)
print("Total Digit : ",digit)
print("Total Space : ",space)
print("Total Special Character : ",special)
        
