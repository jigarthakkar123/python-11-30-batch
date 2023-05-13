l=[]

for i in range(1,1001):
    if i%7==0 and i%5!=0:
        l.append(i)

print(l)


d={}
value=1
for i in "Hello":
    if i in d:
        d[i]=value+1
    else:
        d[i]=value
print(d)
