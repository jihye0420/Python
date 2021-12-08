f = open("input.txt","r")
list=[]
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    list.append(line)
    # print(line)
    # print(list)
f.close()


def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print("가장 긴 단어는 "+longest_word+"입니다.")

list = line.split()  
find_longest_word(list)  