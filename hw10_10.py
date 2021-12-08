# while True:
#         try:
#                 fname = input("입력 파일 이름: ")
#                 infile = open(fname, "r") 
#                 break
#         except IOError:
#                 print("파일 " + fname + " 이 없습니다. 다시 입력하시오.")

infilename = input("파일 이름을 입력하시오: ")
f = open(infilename,"r")
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
f.close()

word_1 = line.count(' ')
word_2 = line.count('    ')
word_1 = word_1 - word_2*4
print("스페이스 수 = "+str(word_1)+", 탭의 수 = "+str(word_2))
