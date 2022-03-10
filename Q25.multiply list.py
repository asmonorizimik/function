# multiply_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
# [10, 200, 150, 100]
def list_change(list1,list2):
    i=0
    a=[]
    while i<len(list1 or list2):
        mul= list1[i]*list2[i]
        i+=1
        a.append(mul)
    print(a)
        
list_change([5,10,50,20],[2,20,3,5])
