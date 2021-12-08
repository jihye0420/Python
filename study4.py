"""
 반복문
"""
#1.for in문
"""팩토리얼 계산하기"""
# n=int(input("정수 입력:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("팩토리얼:",fact,"이다!")

#2.while문
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

#이중 for문
for i in range(10):
    for j in range(3):
        print("*", end=" ")
    print()
