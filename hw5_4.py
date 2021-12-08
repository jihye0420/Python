def getGrade(score):
    if score>=90:
        grade="A"
    elif score<90 and score>=80:
        grade="B"
    elif score<80 and score>=70:
        grade="C"
    elif score<70 and score>=60:
        grade="D"
    else :
        grade="F"
    return grade

score=int(input("점수를 입력하세요: "))
result=getGrade(score)
print("성적은 ", result, "입니다.")