"""
 자료구조((data structure)=데이터구조): 자료들을 저장하는 여러가지 구조들
 *시퀀스(sequence)
 -요소로 구성
 -순서
 -번호(접근 가능한 인덱스)
 -6개의 내장 시퀀스(str(불변), bytes(불변), bytearray(가변), list(가변), tuple(불변), range(...?))
 -가변 객체-리스트, 셋, 딕셔너리, 바이트배열
 -불변 객체-숫자, 문자열, 튜플
 -중요 타입-문자열, 바이트배열, 리스트, 셋, 딕셔너리, 튜플
 -**중요
  동일한 연산 지원-인덱싱, 슬라이싱, 덧셈 연산, 곱셈 연산 / 내장함수 적용가능(len(),min(),max() 등)
"""

"""
 튜플(tuple): 리스트와 동일, 하지만, 불변!!!
 -장점 및 비교
 리스트: 가변 객체 / 딕셔너리에서 키로 사용 불가 
 튜플: 불변 객체 / 딕셔너리에서 키로 사용 가능 / 반복 처리 속도 빠름
"""
# a=tuple()
# b=list()
# a=("안녕", 1, 3, 'ㅎ')
# print(a)
# #a[0]=1 #튜플은 불변 객체
# print(a[0])
# b+=[1,3,4,5,5,6]
# print(b)

# #요소가 하나인 튜플을 만들 때, 쉽표가 없으면! 그냥 수식, 문자열이다.  / 쉼표가 있어야! 튜플이 된다.
# a=(1)
# print(a)
# b=("안녕~!")
# print(b) #string이 됨!
# c=("앗녕!!!",) #주의! 쉼표가 있어야! 튜플이 됨!!!
# print(c)

# #튜플<->리스트
# a=[1,2,4]
# b=(3,4,5)
# print(tuple(a))
# print(list(b))

# #튜플 추가 연산들
# a=("안녕ㅎㅎ", [10,20,30], 1)
# a+=("추가1", "추가2")
# print(a)
# print(*a) #불변 객체이나, 다른 튜플에 합치는 것은 가능 -> 기존이 아닌 새로운 튜플 생성하는 것!
# b=(1,)*3 #곱셈 연산 가능
# print(b)
# a[1][2]=40 #튜플 안의 리스트 변경 가능
# print(a)
# c=[1,23]
# c+=(56,4) #리스트에 튜플 합치기 가능(하지만, 리스트가 됨)
# print(c)
# #d=(12,15)
# #d+=[11,23] #튜플에 리스트를 합치는 것은 불가능! =>에러남!
# #print(d)

# #튜플 패킹과 언패킹
# t=(1,2,3)
# a,b,c=t
# print(t)
# print(a,b,c)

# #enumerate() => 나열
# a=[1,2,4]
# for i,j in enumerate(a): #i=index, j=value
#     print(i,j)

"""
 세트(set): 순서x, 중복x => 집합과 동일, 위치별로 접근 불가능!!!(순서가 없으므로-indexing못함)
"""
# a=set() #공백 세트!
# c={} #공백 딕셔너리!
# print(a)
# print(c)
# b={2,34,4}
# print(b)

# #세트<->리스트
# #a={[1,2,3,1,1,1,1]} #에러=>리스트가 세트가 되기 위해서는 set함수를 이용해야함!
# a=set([1,2,3,1,1,12,2,3]) #set함수 이용->리스트->세트 됨
# print(a)
# b=set("안녕하세요~")
# print(b)

#세트 연산-all():모든 요소가 True이면 True / any():하나라도 True이면 True, enumerate(), len(), min(), max(), sorted(), sum() 사용가능!

# #세트 요소 추가하기
# a={1,2,3}
# a.add("하이")
# print(a)
# a.remove(3) #삭제하려는 요소가 없으면! 예외발생!!!, 발생시키지 않으려면 discard()사용!
# #a.remove("hi")
# print(a)
# a.discard("hi")
# print(a)

# #세트 함축 연산-리스트 필요(순서가 없으므로 인덱싱 필요!~)
# list=[1,2,3,4,5,4,6,6,6,6,7,6]
# result={x for x in list if x%2==0}
# print(result)

# #집합연산 가능 
# # -부분집합(>=,>,<=,<) a>=b(a가 b의 부분집합?(a=b같아도 가능)) / a.issubset(b)=>true(a=b포함),false(a=b포함하지 않음)
# a={1,2}
# b={1,2,3,4}
# c={1,2}
# if a<b :
#     print("a가 b의 부분집합이다.")
# if a.issubset(b):
#     print("a가 b의 부분집합이다.")
# if a<c :
#     print("1.a가 c의 부분집합이다.")
# if a.issubset(c):
#     print("2.a가 c의 부분집합이다.")

#==, !=, 합집합(|, a.union(b)), 교집합(&, a.intersection(b)), 차집합(-, a.difference(b))

"""
 리스트<->세트
"""
# a=[1,2,3,3,3,4,2]
# b={10,20,30,1,2,3}
# c=[3,4,5,6,7]
# print(list(b))
# print(set(a))
# #서로 다른 정수의 개수
# print(len(set(a)))
# #공통 정수
# print(set(a)&set(b))

"""
 문자열의 공통 문자=>사용자 2개 문자열 입력받아서 공통 문자 출력하기
"""
# a=set(input("문자1 입력:"))
# b=set(input("문자2 입력:"))
# print(f"문자1:{a}")
# print(f"문자2:{b}")

# c=a&b
# print("공통적인 문자:",end=" ")
# for i in c:
#     print(i, end=" ")
# print()
    
"""
 문자열의 공통 문자=>중복되지 않은 단어의 개수 세기
"""
txt=input("입력:")
print(txt)
words=txt.split(" ") #띄어쓰기를 기준으로 문자열을 자름!=>리스트로 저장됨!(리턴!)
print(words)
unique=set(words)

print("사용된 단어의 개수=", len(unique))
print(unique)
