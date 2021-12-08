a=[1,2,3,4,5]
b=[1,3,3,4,5,6,7]
print("a=", a)
print("b=", b) 
new=[x for x in a if x in b]
print("new=", new)

