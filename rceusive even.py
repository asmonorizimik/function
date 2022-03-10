# def even(num):
#     if num>9:
#         i=0
#         s=0
#         while i<num:
#             rem=num%10
#             s=s+rem
#             num=num//10
#         return even(s)
#     else:
#         if num%2==0:
#             print("very even",num)
#         else:
#             print("not even",num)
# even(num=int(input("enter:")))



dict1={1:2,2:3,3:4,4:5}
sum=0
for i in dict1.values():
    sum=sum+1
    print(sum)