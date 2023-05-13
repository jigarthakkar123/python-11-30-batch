d={901:"Nancy",897:"Nirja",654:"Janvi",590:"Raj",432:"Darshan",788:"Kevin",903:"Jainil"}

print(d)
print(d[897])
print(d.get(590))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(432))
print(d)
print(d.popitem())
print(d)
d1={1:"Jainil",2:"Darshan",3:"Varsha",4:"Sid"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
