# class X:
#     def __init__(self, a):
#         self.a=a

# class Y(X):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b=b

# obj=Y(10, " ")
# print(obj.a)

# class Person():
#     pass
# class Student(Person):
#     pass

class X:
    def __init__(self):
        print("X:__init__()")
class Y(X):
    def __init__(self):
        print("Y:__init__()")
y=Y()    

class X:
    def __init__(self, a):
        self.a=a
    def inc(self):
        self.a+=1
    def __str__(self):
        return "VALUE: "+str(self.a)

x=X(20)
print(x)
        
        