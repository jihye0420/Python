# # 리스트 만들기-순서, 중복 가능 / 가변-자동 추가, 삭제 / 어떤 데이터 타입도 가능 
# list=["안녕", 3.12, 50, '이거', "3.14"]
# # 리스트 출력하기
# print(list)
# i=list[1]
# print(i)
# print(list[-2])
# # 언패킹-출력 주의(정말 값을 꺼냄)
# print(*list)
# #-------------------------------------------------------------------------
# # 리스트 방문
# # 1)
# for j in range(len(list)):
#     if j==len(list)-1:
#         print(list[j])
#     else:
#         print(list[j], end=", ")
# # 2) 더 좋은 표현
# for i in list:
#     print(i, end=", ")
# print()
# #-----------------------------------------------------------------
# # zip()함수 => 리스트 합치기
# Q=["첫째", "둘쨰", "셋째"]
# A=["답변1", "답변2", "답변3"]
# A.append("답변4...")
# print(A)
# #두개의 리스트 항목의 개수가 다를 때, 작은 개수의 리스트 개수로 합쳐진다.
# for q,a in zip(Q, A):
#     print(f"질문은 {q}, 답변은 {a}입니다.")
# #-------------------------------------------------------------------
# 리스트 연산 정리
# mylist=["안녕", 3.12, 50, '이거', "3.14"]
# print(mylist)
# mylist[2]=3
# print(mylist)
# mylist.pop(2)
# print(mylist)
# print(mylist.pop(2))
# a=len(mylist)
# print(a)

# list=["안녕", 3.12, 50, '이거', "3.14"]
# #if문에 걸리면 -> elif 실행하지 않음..! 
# # -> why? 인터프리터언어이기때문..?
# if "안녕" in list:
#     print(list)
# elif "하하" not in list:
#     print("NO없어!")
#---------------------------------------------
#에러남->소수와 문자열은 크기 비교 불가..!? 인듯
# list.sort()
# print(list)
#리스트 위치 반환
#print(list.index("3.14"))

# #리스트 삽입
# addlist=["안녕", 3.12, 50, '이거', "3.14"]
# addlist.insert(1, "추가") #숫자 위치에 삽입
# addlist.append("추가2") #끝에 삽입
# mylist=[1, 3, 44, 44.7]
# #내장함수 - min, max를 통해서 리스트 항목의 최대 최소값 출력가능
# #정수, 소수 비교 가능
# #하지만, 소수(float)와 문자열(string) 비교 불가능!
# max=max(mylist)
# min=min(mylist)
# print(max)
# print(min)
# print(addlist)

# a=[1.03, 0.3, 33]
# b=["안녕", "그래", "너는?"]
# # c=["하하", 1] #정렬 불가
# c=[10, 3.7, 4.9]
# #정수, 소수 정렬 가능
# #문자열? -> 사전식으로, 앞의 문자만 비교함.
# a.sort()
# b.sort()
# a.sort(reverse=True) #역순(큰 값이 1등) 정렬
# print(a)
# print(b)
# #내장함수:sorted()-sorting 리스트 return하고 원래 리스트는 변화가 없음
# d=sorted(c) 
# print(c)
# print(d)
# #에러남->print(a.sort()) 또는 
# # sort=a.sort() # print(sort) 출력시 에러남

# #리스트 메소드 정리-list.메소드!
# a=[1, 3, 10, 40]
# b=[50, 51]
# #(method) extend: (self: list, __iterable: Iterable) -> None 
# #vs코드 활용방법 알아보기
# a.extend(b) #b의 리스트 모든 요소를 a의 리스트에 추가
# print(a)
# a.clear() #a의 모든 항목 삭제
# print(a)
# a=[1, 1, 30, 30, 1, 3, 4]
# n=a.count(1) #a리스트에서 값이 몇개가 있는지 확인
# print(n)
# a.reverse() #인덱스를 -1부터 출력
# print(a) 
# b=a.copy() #리스트 복사본 return
# print(b)


#리스트 내장함수 -> min(~) (o) / list.min() (x) 
#ppt 6장 p7

# #리스트 합병과 복제
# list1=[1,2,3]
# list2=[4,5,6]
# #리스트 합병
# list=list1+list2
# print(list)
# #리스트 복제
# list=[1,2,3,4]*12
# print(list)
# resetList=[0]*12
# print(resetList)
# #리스트 비교
# print(list1==list2)
# print(list1<list2)

#**************************************
# #중요-리스트 복사하기
# # =>Shallow copy(메모리 공유) (vs deep copy(메모리 새로 생성))
# tmp=[1,2,3,4]
# tmp2=tmp
# #같은 메모리 공유
# print(id(tmp))
# print(id(tmp2))
# print(f"tmp: {tmp}")
# print(f"tmp2: {tmp2}")
# # =>Deep copy(메모리 공유x, 새로운 메모리 생성)
# tmp=[1,2,3,4]
# tmp2=list(tmp)
# #다른 메모리 공유
# print(id(tmp))
# print(id(tmp2))
# print(f"tmp: {tmp}")
# print(f"tmp2: {tmp2}")

# #리스트 변경 오버헤드 비교 =>ppt참고하기
# # 둘 중 아래가 더 실행속도가 빠르다. 
# # 위는 새로운 메모리를 할당(memory allocation)을 하기 위해서! 시간이 더 많이 소요된다.
# list=list+[i*i]
# list.append()

# #슬라이싱: 원본 리스트는 손상 안됨. 새로운 리스트 생성 => 부분 복사본이 생성된다.
# #deep copy: 메모리 공간 새로 생성
# list=[1,2,3,4,5,6,7,8]
# tmp=list[1:3] #1,3-1=2까지 표현!
# print(id(list))
# print(id(tmp))
# print(tmp)
# tmp2=list
# print(id(list))
# print(id(tmp2))
# print(tmp2)

# #고급 슬라이싱: 없을 시, 디폴트 값: 0, 끝, 1
# #list[start:end:step]
# mylist=[1,2,3,4,5,6,7,8,9,10]
# mylist[0:3]=["1","2","3"] #0,1,2
# print(mylist)
# mylist[::2]=[0,0,0,0,0] #개수가 다르면 가능..? 불가능 에러남. 0부터 2스템
# print(mylist)
    
# mylist=[1,2,3]
# del mylist[-1] #del 리스트의 특정 요소 삭제 =pop과 유사한 기능(pop은 리스트 메소드)
# print(mylist)

"""
 문자열&리스트
 문자열=문자들이 모인 리스트
 인덱스, 슬라이싱 등 리스트와 동일하게 적용
"""
# s="안녕하세요"
# print(s)
# print(s[0])
# print(s[:4])

"""
 불변 객체 -> 함수로 전달
 값만 전달됨 => call by value
"""
# def func(x):
#     #x=42 #x의 값이 바뀌는 지에 따라서 메모리 주소가 달라짐.
#     print(f"id={id(x)}, x={x}")
# y=10
# func(y)
# print(f"id={id(y)}, y={y}")
"""
 가변 객체 -> 함수로 전달
 값&메모리 주소 모두 공유 => call by reference적용됨
"""

"""
 가변 객체: 리스트, 셋, 딕셔너리, 바이트배열
 불변 객체: 튜플, 문자열
 call by value: 값만 전달 => 메모리 주소 공유x -> 불변 객체
 call by reference: 값+주소 전달 => 메모리 주소 공유o -> 가변 객체
 shallow copy: 메모리 주소 공유o -> 가변 객체
 deep copy: 메모리 주소 공유x -> 불변 객체
"""

"""
 조건연산자
"""
# x=int(input("x의 값을 입력하시오: "))
# print(f"x={x}")
# #중요! 여기서는 괄호가 필요함!
# y=(x*x if x>5 else x)
# print(f"y={y}") 

"""
***********************************************
 리스트 함축(list comprehension)
************************************************
"""
# #리스트 초기화1
# list=[]
# for x in range(10):
#     list.append(x*x)
# print(list)
# #=리스트 함축!***
# list2=[x*x for x in range(10)]
# print(list2)
"""중요"""
# #리스트 함축(순서=출력식+반복문(for문)+조건문(if문)=>여러번 사용도 가능) #일반식 쓰는 순서=>순서대로
# #2.조건문과 반복문 순서가 중요함(if문과 for문 순서로 작성하려는 경우는 if-else문 가능) #일반식 쓰는 순서=>뒤에서 앞으로
# #3.반복문 여러번 쓰는 경우-1번 for문 2번 for문 => 처리순서 2번=뒤(제일 바깥for)->1번=앞(안for) #일반식 쓰는 순서=>순서대로
""""""

# list3=[x*x for x in range(10) if x%2==0]
# print(list3)
# #=
# list4=[]
# for x in range(10):
#     if x%2==0:
#         list4.append(x*x)
# print(list4)

"""2"""
# test=[x*x if x%2==0 for x in range(10)] #에러가 남-> 조건문과 반복문 순서가 중요함(if문과 for문 순서로 작성하려는 경우는 if-else문 가능)
# print(test)
# 출력결과가 위와 조금 다름 - 의미가 조금 다름------------------------------------------
# listAll=[x*x if x%2==0 else x for x in range(10)]
# print(listAll)
# ------------------------------------------------------

#*****************************************
#다양한 리스트 함축-중요
#*****************************************
# list=[1,2,3,4,5,6,7,8,9,10]
# temp=[i if i>5 else 0 for i in list]
# print(list)
# print(temp)

# #=
# temp2=[]
# for i in list:
#     if i>5:
#         temp2.append(i)
#     else:
#         temp2.append(0)
# print(temp2)

"""3"""
# a = [i * j for j in range(2, 10) for i in range(1, 10)]
# print(f"a={a}")
# b=[]
# for j in range(2,10):
#     for i in range(1, 10):
#         b.append(i*j)
# print(f"b={b}")

"""서로 같은 표현"""
# #일반식
# a=[]
# for x in range(100):
#     if x%2==0 and x%3==0:
#         a.append(x)
# print(a)
# #=
# #리스트 함축
# b=[x for x in range(100) if x%2==0 and x%3==0]
# print(b)

"""
 다차원
 n차원 리스트=n-1차원 리스트의 (1차원) 리스트
 3차원 리스트=2차원 리스트의 (1차원) 리스트
 2차원 리스트=1차원 리스트의 (1차원) 리스트
"""

"""
 2차원 리스트=2차원 배열과 동일
 행(가로=rows->x=>m)
 열(세로=cols->y=>n)
 #행마다 열의 길이가 달라도 됨
 #c++배열과 차이!=>모든 메모리가 꽉차지만 파이썬은 꽉차지 않아도 됨(행마다 열의 길이가 달라도 됨)=>(동적 메모리 할당)dynamin allocation
 #리스트의 리스트=>레퍼런스 변수=>내부 메모리 구조!
"""
"""1"""
# a=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]
# print(a)

"""2"""
# rows=3 
# cols=5 #3x5리스트
# a=[]
# b=[]
# c=[]
# s=[]
# #rows의 값만으로의 [리스트 복제]를 이용한 2차원 리스트 생성
# for row in range(rows):
#     b+=[[0]*row]
# print(b)
# #cols의 값으로의 [리스트 복제]를 이용한 2차원 리스트 생성
# for row in range(rows):
#     a+=[[0]*cols] #[리스트 복제]
# print(a)
# """같은 표현으로 리스트 함축 이용하기"""
# s=[([0]*cols) for row in range(rows)]
# print(s)
# #1차원 리스트만들기=>3x5 리스트
# for row in range(rows):
#     #[]이거 빠진것
#     c+=[0]*cols
# print(c)

"""3. 2차원 리스트 요소 접근"""
a=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
#행과 열의 개수를 구함
rows=len(a)
cols=len(a[0])

for row in range(rows):
    for col in range(cols):
        print(a[row][col], end=",")
    print()
"""도전과제인걸로...!=>인덱스가 -1일때는 , 출력하지 않도록 하기"""
# for row in range(rows):
#     for col in range(cols):
#         if cols-1 == -1:
#             print(a[row][col])
#             print()
#         else:
#             print(a[row][col], end=",")
#     #print()

"""
 3차원 리스트=2차원 리스트의 1차원 리스트
 #c++배열과 차이!=>모든 메모리가 꽉차지만 파이썬은 꽉차지 않아도 됨(행마다 열의 길이가 달라도 됨)=>dynamin allocation
"""

# b=[
#     [[1,2],[3,4,5],[6,7]],
#     [[1],[5,6,7],[3]],
#     [[4],[4,5]]
# ]
# print(b)

