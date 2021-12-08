import random

x = random.randint(1, 100)
y = random.randint(1, 100)
operator=random.randint(1, 4)

if operator==1:
    operator=" + "
    answer=x+y
if operator==2:
    operator=" - "
    answer=x-y
if operator==3:
    operator=" * "
    answer=x*y
if operator==4:
    operator=" / "
    answer=x/y

my_answer = int(input(f"{x} {operator} {y} 의 값은?"))

if my_answer==answer:
    print("맞았습니다.")
else:
    print("틀렸습니다.")