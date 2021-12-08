# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age        

class MyClass:
    def __init__(self, radius=10):
        self.radius=radius
    # def set_radius(self, radius):
    #     self.radius=radius
    def display(self):
        print(self.radius)

t=MyClass()
a=MyClass(13)
t.display()
a.display()