subject_marks = [('국어', 88), ('수학', 90), ('영어', 99), ('자연', 82)]
print("원래의 리스트:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\n정렬된 리스트:")
print(subject_marks)