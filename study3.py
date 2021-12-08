"""
 제어문 
 -조건문: 만약에 조건문이 참일때 실행
    1. if문
    2. if-else문
    3. if-elif-else문
 -제어문: ~동안에(조건문이 참인 동안에) 실행
    1. while문
        while-else문
    2. for in문
        for in-else문
"""

"""
 조건문
 -괄호 없음
 -:필요
 -들여쓰기
 -
"""
# a=5
# if a>4:
#     print(a)
# else:
#     print("호호")

# #실수 비교는 에러남(실수와 실수끼리의 비교는!)
# a=5
# if a==5.0000:
#     print(a)
# else:
#     print("호호")

"""실수 비교"""
"""
 Round-off error: 컴퓨터가 표현할 수 있는 비트의 수가 제한
 =>부족한 값은 정확하게 표현x
 컴퓨터는 근사한 사람을 좋아해.(근삿값으로 출력~!)
"""
# from math import sqrt
# #import math
# #import sqrt
# #math.sqrt()
# n=sqrt(3.0) #루트(3.0)
# if n*n==3.0:
#     print("같다!")
# else:
#     print("다르다!") #다르다고 출력!
"""해결"""
# if abs(n*n-3.0)<0.0000001:
#     print("같다~")

"""
 True, False
 False: 0 또는 빈 값은 모두!
"""
x=0
bool(x)
print(bool(x))
"""
 1. 정수
 -정수에 쉼표 사용 불가!-> 사용시 튜플의 값을 얻음
 2. 정수
 -int("실수str") -> 에러
 3. 정수
 -파이썬 아주 큰 정수도 처리 가능!
"""
# #튜플
# a=1,000,000
# print(a)
# #언더바->숫자 구분 가능
# a=1_000_000
# print(a)
# #진수

"""2."""
# x=int(True)
# print(x)
# x=bool(1)
# print(x)
# x=int(98.8)
# print(x)
# x=int("99")
# print(x)
"""실수 sring은 에러"""
# x=int("99.99")
# print(x)

"""조건 연산자=>괄호 필요!!!!*중요"""
# x=int(input("입력:"))
# a=(x if x>0 else 0)
# print(a)

country=input("나라:")
age=int(input("나이:"))
#문자열 비교 가능! 다른언어: 객체.equals("~")로 표현해야함.
if country=="한국" and age==23:
    print("이거 맞아요~")
#20<=age<=45 ->이런 표현식도 가능! 
#조건문은 한번 실행하면 빠져나감!=if-elif일때! if-if일때는 모두 검사!
if age==20:
    print("새낸기")
elif 20<=age<25:
    print("대학생")
else:
    print("안녕")

#실수끼리 연산->아주 작은 오차도 있을수 있음!!! 딱떨어질수 없음!=>연산 정답출력시 정답있을수있음.