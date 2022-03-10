
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upper= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
        'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
def strong_password():
    password=list(passwd)
    if len(password)>6 and len(password)<=16:
        i=0
        while i<len(password):
            if password[i] in (str(digits) or lower or upper or symbols):
                if password[i]in str(digits) and password[i] not in (lower or symbols):
                    print("not strong, put mix characters")
                    break
                elif password[i] in lower and password[i] not in (str(digits) or symbols):
                    print("you still need to use more characters")
                    break
                elif password[i] in symbols and password[i] not in(str(digits) or lower):
                    print("use letters also")
                    break
                else:
                    print("strong password")
                    break
            else:
                print("valid")
                break
            i+=1
    else:
        print("not valid")
passwd=input("enter: ")
strong_password()
 
 