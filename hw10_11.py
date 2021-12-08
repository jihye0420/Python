##
#이 프로그램은 파일의 각 줄의 앞에 번호를 붙인다. 
#

infile  = open("proverbs.txt")
outfile = open("output.txt","w")

i = 1

for line in infile:
    outfile.write(str(i) + ": " + line)
    i = i + 1

infile.close()
outfile.close()