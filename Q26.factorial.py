def factorial(n):
    f=1
    i=1
    while i<=n:
        f=f*i
        i+=1
    print(f)
factorial(n=int(input("enter the number:")))