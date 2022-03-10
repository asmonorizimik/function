
##5 Types of Arguments in Python Function Definition:

#1.DEFAULT ARGUEMENT: default arguement are value that are provided while definding functions.
#It used assingnment opperator "=" to assign the default value to the arguement
##default value means value assign to varaible.
## example:
# def add(a,b=5,c=9):
#     return a+b+c
# # print(add(3))##giving only one mandatory element
# # # print(add(3,5,6))##give all the arguements
# print(add(3,4))##giving one of the optional arguements


# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")
##default values are evaluate only once at the point of the function definition in the defining scope


##SCOPE=>1. global scope : define the value outside the function
##       2.local scope : define the value inside the function



# With keyword arguments, as long as you assign a value to the parameter, the positions of the 
# arguments do not matter. ... Default arguments are keyword arguments whose values are assigned
# at the time of function definition.

#2.KEYWORD ARGUEMENTS: 
##In keyword arguement,the value passed through arguement does not need to be in orders, but
##all the arguement should match the parameters in the function definition. 
##EG. 

# def function_name(a,b=5,c=9):
#     return a+b*c
# print(function_name(b=2,c=6,a=2))###changes the order
# # print(function_name(a=3))##giving only mandatory arguement as keyword arguement.
# ##does'nt follow their position
# ##since the parameter is  given as keyword arguement, all arguments needs not to be in order. 

# def data(name,age,school):
#     print(name,"age:",age,"studied in ",school)
# data(age=18,name="Anu",school="NG")



##3.POSITIONAL ARGUEMENTS:In positional,during function call, value pass through arguements should
#be in the order of parameter in the function definition.
# def add(a,b,c):
#     return a+b*c
# print(add(1,2,3))
# # print(add(2,c=4,b=2))





##VARIABLE_LENGTH ARGUEMENTS/ ARBITRARY ARGUEMENT:
#If we dont'n know the number of arguements needed in a function, we can use arbtrary arguement.
##this arguement will be wrapped up in a tuple.

#4. ARBITRARY POSITIONAL ARGUEMENT:For arbitrary positional arguement, an asterisk("*args") is placed
#before a parameter,which can hold non- keyword variable length arguements.
#eg:
# def fname(*a):
#     result = 0
#     for i in a:
#         result+=i
#     return result
# print(fname(1,2,3,4,5,6,7))
# print(fname(10,20))


# def numbers(*a):
#     i=0
#     while i<=len(a):
#         print(i)
#         i+=1
# numbers(1,2,3,4,5,6,7,8,9,10)


# def icecream(*flavours):
#  for flavour in flavours:
#   print("I love",flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")



# def greet(*names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")





# 5. ARBITRARY KEYWORD ARGUEMENTS:For arbitrary keyword arguement,a double asterisk ("**kwargs") is 
#placed before a parameter in function definition which can hold keyword variable length arguements.
##eg:
# def fname(**a):
#     for i in a.items():
#         print(i)
# fname(n=5,colour="blue",fruits="blueberry")


#  def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for arg in kwargs.values():
#         result += arg
#     return result
# print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
