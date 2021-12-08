import random

n=1000000
count=0
for i in range(n):
  x=random.random()
  y=random.random()
  if(x*x+y*y<1):
    count=count+1
a=4*count/n
print("파이의 값은",a,"입니다.")