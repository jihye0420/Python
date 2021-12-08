before_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("실행 전: ",before_numbers)
after_numbers=[-x if 3<=x<=8 else x for x in before_numbers]
print("실행 후: ",after_numbers)