def testPrime(n):
    num=2
    while num<=n:
        i=2
        while num%i:
            i+=1
        if i==num:
            print(num, end=" ")
        num+=1
    return

testPrime(100)