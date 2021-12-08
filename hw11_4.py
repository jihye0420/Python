num=[1,2,3,4,5,6,7,8,9,10]
print("원래 리스트: ")
print(num)
print("짝수: ")
print(list(filter(lambda x:x%2==0, num)))
print("홀수: ")
print(list(filter(lambda x:x%2, num)))