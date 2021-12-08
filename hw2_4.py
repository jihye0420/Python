hour=int(input("시간을 입력하시오:"))
miniute=int(input("분을 입력하시오:"))
second=int(input("초를 입력하시오:"))
seconds=(hour*3600)+(miniute*60)+second
print(hour,"시간",miniute,"분은",second,"초는",seconds,"초입니다.")


seconds=int(input("초를 입력하시오:"))
hour=seconds//3600
seconds-=3600*hour
min=seconds//60
seconds-=60*min
print(hour,"시간",min,"분",seconds,"초입니다.")