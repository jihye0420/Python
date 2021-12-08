try:
    myList=[0]*10
    e=myList[10]
    print("처리 종료")
except IndexError:
    print("인덱스 오류")