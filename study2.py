"""
 변수: 변하는 값이나 수를 표현 => 메모리 공간에 이름 붙이는 것-이 공간에 값을 저장할 수 있음
 *중요* 어떤 데이터 타입(자료형)도 저장 가능=>할당문일때, 메모리 할당 => Dynamin memory allocation - 참조형, 주소형, 포인터
 *c++/java: 할당 전 데이터 타입 지정해야함! => Static memory allocation
 -객체 형태로 메모리에 저장(객체로 래핑) -> 변수에는 객체를 참조할 수 있는 값 저장
 *call by reference! 가능!

 -변수 이름
    의미있는 이름 사용!
    문자, 언더바, 숫자 가능
    공백, 기호, 예약어 불가능
    숫자로 시작은 불가능!
    대소문자 구분함
    낙타체
"""

"""
 자료형
 -숫자, 부울형, 시퀀스 등
 -불변 객체(문자열,튜플) vs 가변 객체(바이트배열,리스트,셋,딕셔너리)
"""
# x=100
# y=x
# print(id(x)) #주소 출력
# print(id(y)) #같은 주소 출력=>x의 메모리 주소가 복사
# print(type(x)) #자료형 출력

# a=100
# b=10
# c=58.3
# d=33
# print(a/b) #실수 나눗셈
# print(a//b) #정수 나눗셈
# print(c-d) #정확하게 계산되지 않음 => **중요! Round-off error(컴퓨터는 근사한 사람을(실수.000001) 좋아해~)

"""
 타입(형)변환
 -자동형변환
 -강제형변환
"""
# #강제형변환
# x=12.2
# x=int(x)
# print(x)

# y=1.3
# z=round(x*y,2) #소수점 2째자리까지 표현=>3째자리에서 반올림!
# print(x*y)
# print(z)


"""
 숫자<->문자열
"""
# #에러-자동형변환이 지원하지 않음!
# #a="hi"+2
# #해결!-강제형변환!
# a="hi"+str(2)
# print(a)

"""
 입력-input()함수=>string으로 입력됨
"""
# test=input("입력:")
# print(type(test))


"""
 형식화된 출력!
"""
# py=3.14113
# print(py)
# print("%10.3f"%py) #전체칸수:10, #소수점이하:3#f:실수, d:정수, s:문자열

"""파이썬 변수, 객체 참조횟수=해당 객체를 가리키는 이름의 수, 가비지콜렉터=파이썬은 자동으로 메모리를 삭제한다.1)객체 참조횟수=0->삭제 2)접근 불가능한 객체를 삭제!"""

"""hw2_4=>초를 입력받아 일,시간,분,초로 변환"""
days=int(input("일을 입력하시오:"))
hour=int(input("시간을 입력하시오:"))
miniute=int(input("분을 입력하시오:"))
second=int(input("초를 입력하시오:"))
seconds=(days*60*60*24)+(hour*3600)+(miniute*60)+second
print(hour,"시간",miniute,"분은",second,"초는",seconds,"초입니다.")

"""
 초->분->시->일
 일*24시->시*60분->분*60초->초
"""
seconds=int(input("초를 입력 하시오:"))
days=seconds//(60*60*24) #//정수 나눗셈
seconds-=(60*60*24)*days 
print(seconds)
hour=seconds//(60*60) #1시간=60분 1분=60초 이므로 1시간=60*60초
seconds-=(60*60)*hour
min=seconds//60 #1분=60초
seconds-=60*min
print(days,"일",hour,"시간",min,"분",seconds,"초입니다.")