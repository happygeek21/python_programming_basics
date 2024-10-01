def fibo(timeszzz):
    fibs = []
    a,b = 0,1
    c= 100

    for _ in range(times):
        fibs.append(a)
        a = b
        b = a+b
    return c
    

times=int(input("How Many Interations for Fibonacci? Enter No: "))
result= fibo(times)
print(times)
print("Fibo Starting with 1:",result)