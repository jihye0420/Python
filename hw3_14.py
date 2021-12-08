import math
a=int(input("a를 입력하시오: "))
b=int(input("b를 입력하시오: "))
c=int(input("c를 입력하시오: "))
r=b**2-4*a*c

if r>0:
    answer1 = (-b+math.sqrt(r))/(2*a)
    answer2 = (-b-math.sqrt(r))/(2*a)
    print(f"2개의 실근입니다. 실근은 {answer1}과 {answer2}입니다.")
if r==0:
    answer = -b/(2*a)
    print(f"하나의 실근입니다. 실근은 {answer}입니다.")
if r<0:
    print("실근이 존재하지 않습니다.")
