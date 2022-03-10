
###1. capitalize

# def solve(s):
#     x=s.split()
#     print(x)
#     a=''
#     for i in x:
#         a=a+i.capitalize()+' '
#     return a
# s="welcome to my home"
# a=solve(s)
# print(a)


##2. find the string

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):   
#         if (string[i:i+len(sub_string)] == sub_string):
#             count += 1
#     return count
# string="abcdcdc"
# sub_string="cdc"
# a=count_substring(string,sub_string)
# print(a)
   

###3.name and marks (harry berry)
# r=[]
# s=[]
# for _ in range(int(input("enter the number"))):
#     name = input("name:")
#     score = float(input("marks"))
#     r+=[[name,score]]
#     s+=[score]
# b=sorted(list(set(s)))[1]
# for a,c in sorted(r):
#     if c==b:
#         print(a)



###4.divmod() method brings the quotien and the remainder

# a=int(input( "enter the number here:"))
# b=int(input( enter the divisor:))
# print(a//b)
# print(a%b)
# print(divmod(a,b))



##5. loops...square of the digits....if input is 3 ..output-0,1,4

# n = int(input("enter: "))
# i=0
# while i<n:
#     print(i*i)
#     i+=1



###6.swap the case...all lower case turns upper case and vise versa...

# def swap_case(s):
#     c=s.swapcase()
#     return c
# s="Hackerank.com presents Pythonist 2"
# x=swap_case(s)
# print(x)



###7. join the string words with hyphen...

# def split_and_join(line):
#     line=line.split()
#     print(line)
#     line="-".join(line)
#     return line
# line="this is a string"
# a=split_and_join(line)
# print(a)




##8.print function ..input 3...output-1,2,3

# num = int(input())
# i=1
# s=""
# while i<=num:
#     s=s+str(i)
#     i+=1
# print(s)


##9.runner up input 23665.... output-5

# n = int(input("enter:"))
# array = map(int, input("enter").split("entterrrr:"))
# array=sorted(array,reverse=True)
# for i in range(len(array)):
#     if array[i]==array[0]:
#         continue
#     else:
#         print(array[i])
#         break


##10. compare list

# def compare_lists(llist1, llist2):
#     if llist1==llist2:
#         return 1
#     else:
#         return 0
# llist1=[1,2,1,6]
# llist2=[1,2,1,2]
# a=compare_lists(llist1,llist2)
# print(a)
        


## (i) array=["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
## output='b***i***t***c***o***i***n***'
# array=["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
# array.sort()
# i=0
# while i<len(array):
#     j=0
#     while j<len(array[i]):
#         print(array[i][j],end='***')
#         j+=1
#     if i or j>1:
#         break
#     i+=1



###super digit:----
# def digSum( n):
#     sum = 0
#     while n > 0 or sum > 9:
#         if n == 0:
#             n = sum
#             sum = 0
#         sum += n % 10
#         n //= 10
#     return sum
# n=int(input("enter the number:"))
# # n = 9875987598759875
# # n=148148148
# # n=123123123
# print(digSum(n))