def getMoneyText(amount):
    one = "일이삼사오육칠팔구"
    unit = [" "]+list("십백천")
    result = []
    i=0
    while amount > 0:
        amount, r = divmod(amount, 10)
        if r > 0:
            result.append(one[r-1]+unit[i])
        i+=1
    return ''.join(result[::-1])


goal = 1000

while(1):
    money = int(input("1000이하의 금액을 입력하시오: "))

    if money <= goal:
        break

result = getMoneyText(money)
print(result+"원")
