def kbc(Q,opt,ans):
    i=0
    a=0
    while i<len(Q):
        print(i+1,Q[i])
        j=0
        while j<len(opt):
            print("  "+str(j+1)+":",opt[i][j])
            j+=1
        answer=int(input("enter your ans: "))
        if answer==ans[i]:
            print("CONGRATS")
        elif answer==5050:
            if a==0:
                b=0
                while b<len(fifty_life[i]):
                    print("  "+str(b+1)+":",fifty_life[i][b])
                    b+=1
                a+=1
                ans5050=int(input("enter your answer 5050: "))
                if ans5050==fiftyans[a]:
                    print("correct answer ")
                else:
                    print("wrong answer ")
                    break
            else:
                print("you already used 5050 lifeline\n")
                n=int(input("enter:"))
                if n==ans[i]:
                    print("CONGRATS you won the game with 5050")
                else:
                    print("Opps sorry!!!")
                    break

        else:
            print("wrong answer\ngame over")
            break
        i+=1
Q =[
"Who is the founder of Python Language?",
"Who discovered Javascript?",
"Who is the founder of Java Language?",
"Who invented Computer?"
]

opt= [
["Benjamin","Thomas A.E","Guido Van Rossum","Robert Fulto"],
["Elexander", "Nicola Tesla","Leonardo","Brenden Eich"],
["James Gosling", "Louise Pastuer", "Flaming", "Clement Eder"],
["Flaming","Charles Babbage","Adam Osborn","Angela B"]
]
ans = [3,4,1,2]

fifty_life=[
["Robert ","Guido Van Rossum"],
["Nicola Tesla","Brenden Eich"],
["Clement Ader","James Gosling"],
["Charles Babbage","Adam Osborn"]
]
fiftyans=[2,2,2,1]

kbc(Q,opt,ans)

