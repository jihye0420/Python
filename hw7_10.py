set1={10,20,30,40,50,60}
set2={30,40,50,60,70,80}
set3=set1&set2
setAll=(set1|set2)-set3
print("첫 번째 세트",set1)
print("두 번째 세트",set2)
print("어느 한쪽에만 있는 요소들",setAll)