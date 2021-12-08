# from tkinter import *
# window=Tk()

# id, passwd = StringVar(), StringVar()


# def check_data():
#     if id.get() == "20181054" and passwd.get() == "1234":
#         print("Logged IN Successfully")
#     else:
#         print("Check your Usernam/Password")



# Label(window, text="아이디").grid(row=0, column=0)
# Label(window, text="패스워드").grid(row=1, column=0)

# id=Entry(window, textvariable=id).grid(row=0, column=1)
# passwd=Entry(window, textvariable=passwd).grid(row=1, column=1)

# Button(window, text="로그인", command=check_data).grid(row=2, column=0)
# Button(window, text="취소").grid(row=2, column=1)

# window.mainloop()

# tkinter를 사용하기 위한 import
from tkinter import *
from tkinter import ttk

# tkinter 객체 생성
window = Tk()

# 사용자 id와 password를 저장하는 변수 생성
user_id, password = StringVar(), StringVar()

# 사용자 id와 password를 비교하는 함수
def check_data():
    if user_id.get() == "20181054" and password.get() == "1234":
        print("Logged IN Successfully")
    else:
        print("Check your Usernam/Password")



# id와 password, 그리고 확인 버튼의 UI를 만드는 부분
ttk.Label(window, text = "아이디 : ").grid(row = 0, column = 0)
ttk.Label(window, text = "패스워드 : ").grid(row = 1, column = 0)

ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1)
ttk.Entry(window, textvariable = password).grid(row = 1, column = 1)

ttk.Button(window, text = "로그인", command = check_data).grid(row = 2, column = 0)
ttk.Button(window, text = "취소").grid(row = 2, column = 1)

window.mainloop()