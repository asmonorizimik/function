
def string(str1,str2):
    i=0
    while i<len(str1 or str2):
        if len(str1)>len(str2):
            return str1
        elif len(str1)==len(str2):
            return str1,str2
        else:
            return str2
        i+=1
str1=input("enter str1: ")
str2=input("enter str2: ")

print(string(str1,str2))