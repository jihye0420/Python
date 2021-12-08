num=2
while num<=20:
    divisor = 2
    prime=True
    while divisor<num:
        if num%divisor==0:
            prime=False
            break;
        divisor+=1
    if prime:
        print(num, end=" ")
    num+=1