l=[1,2,1.1,2.2,"tops",True,"python",10,1,2]

print(l)
l.append(100)
print(l)
l1=l.copy()
print(l1)
print(l.count(1))
l2=[101,102,103]
l.extend(l2)
print(l)
print(l.index(10))
l.insert(5,"Java")
print(l)
print(l.pop())
print(l)
print(l.pop(3))
print(l)
l.remove(1.1)
print(l)
l.reverse()
print(l)
