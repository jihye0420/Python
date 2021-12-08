txt=input("문자열을 입력하시오:")
noTxt=input("금칙어를 입력하시오:")

txt=txt.split()
noTxt=noTxt.split()

clean=[]

for i in txt:
    #print(i,end=",")
    if i in noTxt:
        i=i.replace(i, "*"*len(i))
    clean.append(i.strip())
oneline=" ".join(clean)
print(oneline)