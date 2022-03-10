# def perfect_number(number):
#     i=1
#     sum=0
#     while i<number:
#         if number%i==0:
#             sum+=i
#         i+=1
#     if sum==number:
#         print("perfect number")
#     else:
#         print("not")
# number=int(input("enter the number: "))

# perfect_number(number)


def perfect_number():
    i=1
    while i<=1000:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum+=j
            j+=1
        if sum==i:
            print(i,"perfect number")
        i+=1
perfect_number()
