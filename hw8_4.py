class Rectangle:
   def __init__(self, x, y, width, height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height

   def __str__(self):
      return "("+str(self.x)+","+str(self.y)+","+str(self.width)+","+str(self.height)+")"

   def setX(self, x):
      self.x = x

   def getX(self):
      return self.x

   def setY(self, y):
       self.y = y

   def getY(self):
      return self.y

   def setWidth(self, width):
       self.width = width

   def getWidth(self):
      return self.width

   def setHeight(self, height):
       self.height = height

   def getHeight(self):
      return self.height

   def getArea(self):
      return self.x*self.y

   def overlaps(self, r):
      if self.x > r.x+r.width or self.x+self.width < r.x or self.y > r.y+r.height or self.y+self.height < r.y:
         print("r1과 r2는 서로 겹치지 않습니다.")
      else:
         print("r1과 r2는 서로 겹칩니다.")


r1=Rectangle(0,0,100,100)
r2=Rectangle(10,10,100,100)
r1.overlaps(r2)

    