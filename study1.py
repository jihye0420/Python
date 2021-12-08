#import this

"""객체용 멤버 vs 클래스용 멤버"""
# https://sites.google.com/site/silvercoin99999/java/open_java/class-instance-member 참고

"""hw_5,6,7,8"""
import turtle #turtle 라이브러리

t=turtle.Turtle() # 라이브러리.함수() 실행
t.shape("turtle") # 거북이 모양

t.forward(100) #앞으로 가기
t.width(10) #선의 두께-10
t.color("blue") #선의 색상-파랑색
t.left(90) #왼쪽-90도 회전
t.forward(100) 
t.right(90) #오른쪽-90도 회전
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)

turtle.mainloop()
turtle.bye()


