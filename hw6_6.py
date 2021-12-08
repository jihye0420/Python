a=[1,2,3,4,5,6]
b=[6,7,8,9,10]
print("a=", a)
print("b=", b) 
new=[x for x in a if x in b]
if len(new)>=1:
    print("True")
else:
    print("False")

