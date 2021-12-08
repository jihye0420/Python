before=input("MM/DD/YYYY 형식으로 입력하시오: ")
after=before.split("/")
result=[]
result.append(after[-1])
result.append(after[0])
result.append(after[1])
result="".join(result)
print(result)