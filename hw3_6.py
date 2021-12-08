import random

my_choice=int(input("선택하시오(1:가위 2:바위 3:보) "))
com_choice=random.randint(1,3) #1,2,3의 값을 가져옴 #.range(3) ->0,1,2까지의 값을 가져옴!
print("컴퓨터의 선택(1:가위 2:바위 3:보)", com_choice)

if my_choice==com_choice:
    print("비겼음")
elif my_choice==1 and com_choice==2:
    print("컴퓨터가 이겼음")
elif my_choice==2 and com_choice==3:
    print("컴퓨터가 이겼음")
elif my_choice==3 and com_choice==1:
    print("컴퓨터가 이겼음")
else :
    print("사용자가 이겼음")

