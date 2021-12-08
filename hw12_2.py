class Address:
    def __init__(self, street, city):
        self.street=str(street)
        self.city=str(city)
        
class Person:
    def __init__(self, name, email):
        self.name=str(name)
        self.email=str(email)

class Contect(Address, Person):
    def __init__(self, name, email, street, city, phone):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)
        self.phone=str(phone)

obj=Contect('Kim', 'gh06095@naver.com', 47, '서울', '010-8569-9845')
print(obj.name)
print(obj.email)
print(obj.street)
print(obj.city)
print(obj.phone)