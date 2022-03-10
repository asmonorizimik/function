# question=["Who is the founder of IT?",
# "Which state is the largest state of India?",
# "Who was the first king of India?",
# "Who was the first woman president of India?"]
# fifty_opt=[
# ["Robert Atkinson","Mark K"],
# ["Kerela","Rajasthan"],
# ["Chandragupta Muarya","Krishna Mohan"],
# ["Indira Gandhi","Pratibha Patil"]
# ]
# options=[
# ["Robert Atkinson","Mark Z","Angela B","Ben Harvey"],
# ["Kerela","Rajasthan","Gujarat","Maharastra"],
# ["Maharaj Churachand","Akbar Jhodar","Chandragupta Muarya","Krishna Mohan"],
# ["Indira Gandhi","Pratibha Patil","Sonia Ghandhi","Bakama Naidu"]
# ]

# ans=[1,2,3,2]
# fifty_ans=[1,2,1,2]
# life=0

# def fifty_option(i):
#     global life#used when we want to read or write any global variable value inside the function. 
#     j=0
#     if(life==0):
#         while j<len(fifty_opt[i]):
#             print("  "+str(j+1)+":"+fifty_opt[i][j])
#             j+=1
#         user_fifty=int(input("enter your answer fifty fifty option:"))
#         life+=1
#         if user_fifty==fifty_ans[i]:
#             return True
#         else:
#             return False
#     else:
#         print("You've already used 5050 life")
#         return "next"
# def opt(i):
#     j=0
#     while j<len(options[i]):
#         print("  "+str(j+1)+":"+options[i][j])
#         j+=1
#     user=int(input("enter your answer option:"))
#     if user==ans[i]:
#         return True
#     elif user==5050:
#         return fifty_option(i)
#     else:
#         return False   
# def Q():
#     i=0
#     while i<len(question):
#         print("Q"+str(i+1)+"."+question[i])
#         x=opt(i)
#         if x=="next":
#             i=i-1
#         elif x==True:
#             print("CONGRATULATIONS")
#         else:
#             print("WRONG ANSWER\nYOU LOSE THE GAME")
#             break
#         i+=1
        
# def main():
#     user=int(input("enter 1 to start: \nenter 0 to exit: "))
#     if user==1:
#         print("WISHING YOU ALL THE BEST:)")
#         Q() 
#     else:
#         print("Thank you for trying come and play next time:)")
        
# main()




