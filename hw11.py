# mytuple=(0,1,False)
# print(any(mytuple))

lst_1=['python', 'is', 'easy']
lst_2=[1000,2000,3000]
print(list(zip(lst_1, lst_2)))

print((lambda x: (x+3)*5/2)(3))

num=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2, num)))

lambda x: x*2