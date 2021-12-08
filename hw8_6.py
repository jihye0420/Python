class Person():
    def __init__(self, name, mobile="010-1234-5678", office="1234567", email="name@naver.com"):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        s = ''
        s += self.name + '\n'
        s += "mobile phone:"+self.mobile + '\n'
        s += "office phone:"+self.office + '\n'
        s += "email address:"+self.email + '\n'
        return s

    def setName(self, name):
        self.name = name

    def getName(self):
      return self.name

    def setMobile(self, mobile):
       self.mobile = mobile

    def getMobile(self):
      return self.mobile

    def setOffice(self, office):
       self.office = office

    def getOffice(self):
      return self.office

    def setEmail(self, email):
       self.email = email

    def getEmail(self):
      return self.email


p1 = Person("Kim", office="1234567", email="kim@company.com")
p2 = Person("Park", office="2345678")
p2.setEmail("Park@company.com")
print(p1)
print(p2)
