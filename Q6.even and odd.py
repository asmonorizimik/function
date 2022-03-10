def even_odd(list):
    i=0
    even=[]
    odd=[]
    while i<len(list):
        if list[i]%2==0:
            even.append(list[i])
        else:
            odd.append(list[i])
        i+=1
    # return even,"even list",odd,"odd list"
    print(even,"even list")
    print(odd,"odd list")
    
list=[4,5,3,67,54,2,9,7,4,7,62]
even_odd(list)
# p=even_odd(list)
# print(p)
        
        
